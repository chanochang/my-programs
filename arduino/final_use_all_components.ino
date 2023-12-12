#include <LiquidCrystal.h>
#include <IRremote.h>

#define IR_RECEIVER_PIN 2
#define BUTTON_0 22
#define BUTTON_1 12
#define BUTTON_2 24
#define BUTTON_3 94
#define BUTTON_FUNC_STOP 71
#define EQ 25
#define PLAY 64
#define DOWN 7
#define UP 9
#define POWER 69

#define ECHO_PIN 3
#define TRIGGER_PIN 11

#define LED_GREEN_PIN 6
#define LED_YELLOW_PIN 8
#define LED_RED_PIN 10

#define BUTTON_PIN 24

#define LCD_RS_PIN 28
#define LCD_E_PIN 32
#define LCD_D4_PIN 29
#define LCD_D5_PIN 33
#define LCD_D6_PIN 4
#define LCD_D7_PIN 7

#define PHOTORESISTOR A12

LiquidCrystal lcd(LCD_RS_PIN, LCD_E_PIN, LCD_D4_PIN, LCD_D5_PIN, LCD_D6_PIN, LCD_D7_PIN);

unsigned long lastTimeUltraSensor = millis();
unsigned long ultra_SensorDelay = 60;
double distanceConv = 58.0; //58 for cm, 58/2.54 for in
String distanceType = "cm";

volatile unsigned long timeEchoHigh;
volatile unsigned long timeEchoLow;
volatile bool echoFlag = false;

unsigned long lastTimeWarningBlinks = millis();
unsigned long lastTimeLockBlinks = millis();
unsigned long lastButtonPressed = millis();

int yellowPinState = LOW;
int redPinState = LOW;
byte buttonState = LOW;
bool appLocked = false;

byte remotePressed;
byte screenState = 1;

byte appState = 1;

unsigned long lastTimeLumMeasured = millis();
// unsigned long delayMeasurement = 100;

int lighting;

void triggerUltrasonicSensor(){
  digitalWrite(TRIGGER_PIN,LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN,HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN,LOW);
}

double getUltrasonicDistance(){
  double durationMicro = timeEchoLow-timeEchoHigh;
  double distance = durationMicro / distanceConv;
  return distance;
}

void echoSensorInterrupt(){
  if (digitalRead(ECHO_PIN) == HIGH){
    timeEchoHigh = micros();
  }
  else {
    timeEchoLow = micros();
    echoFlag = true;
  }
}

void warningBlink(int obsDistance){
  unsigned long timeNow = millis();
  unsigned long warningDelay = obsDistance/400 * 1600;
  if ((timeNow- lastTimeWarningBlinks) > warningDelay){
    lastTimeWarningBlinks += warningDelay;
    if (yellowPinState == LOW){
        yellowPinState = HIGH;
    }
    else {
        yellowPinState = LOW;
    }
    digitalWrite(LED_YELLOW_PIN,yellowPinState);
    digitalWrite(LED_RED_PIN,LOW);
  } 
}

void lockLEDs(){
  printLocked();
  bool appLocked = true;
  unsigned long lockDelay = 300;
  unsigned long buttonDelay = 40;
  while (appLocked) {
    unsigned long timeNow = millis();
    if ((timeNow- lastTimeLockBlinks) >= lockDelay){
      lastTimeLockBlinks += lockDelay;
      if (yellowPinState == LOW){
          yellowPinState = HIGH;
          redPinState = HIGH;
      }
      else {
          yellowPinState = LOW;
          redPinState = LOW;
      }
      digitalWrite(LED_YELLOW_PIN,yellowPinState);
      digitalWrite(LED_RED_PIN,redPinState);
    }
    //buttonpin unlock
          Serial.println(buttonState);

    if ((timeNow - lastButtonPressed) > buttonDelay){
      byte newButtonState = digitalRead(BUTTON_PIN);
      if (newButtonState != buttonState){
        if (newButtonState == LOW){
          unlockApp();
        }
      }
      buttonState = newButtonState;
      lastButtonPressed = timeNow;
    }
    // remote unlock
    if (IrReceiver.decode()) {
      IrReceiver.resume();
      int remotePressed = IrReceiver.decodedIRData.command;
      Serial.println(remotePressed);
      if (remotePressed = PLAY){     
        unlockApp();    
      }
    }
  }
  // loop();
}

void unlockApp(){
  appLocked = false;
  echoFlag = false;
  // measureDistance();
  loop();
}

void printWarning(double textToPrint){
  String newtextToPrint = String(round(textToPrint));
  for (int i = newtextToPrint.length(); i < 4; i++){
    newtextToPrint += " ";
  }
  lcd.setCursor( 0, 0);
  lcd.print("Proximity Alert!");
  lcd.setCursor( 0, 1);
  lcd.print("Distance: ");
  lcd.print(newtextToPrint);
  lcd.print(distanceType);
}

void printLocked(){
  lcd.clear();
  lcd.setCursor( 0, 0);
  lcd.print("Activity Locked!");
}

void defaultSettings(){
  lcd.clear();
  lcd.setCursor( 0, 0);
  lcd.print("Default Settings");
  delay(1000);
  appState = 1;
  distanceConv = 58.0;
  distanceType = "cm";
}

// void lcdScreen(){
//   switch (appState){
//     case 1:{
//       measureDistance();
//       break;
//     }
//     case 2:{
//       lcd.clear();
//       lcd.setCursor( 0, 0);
//       lcd.print("Press ON/OFF to ");
//       lcd.setCursor( 0, 1);
//       lcd.print("reset settings  ");
//       break;
//     }
//     case 3:{
//       printLuminosity();
//       break;
//     }
//     default:{
//       measureDistance();
//     }
//   }
// }

void luminosity(){
  unsigned long timeNow = millis();
  unsigned long delayLumMeasurement = 100;
  if ((timeNow - lastTimeLumMeasured) >= delayLumMeasurement){
    lastTimeLumMeasured = timeNow;
    lighting = analogRead(PHOTORESISTOR);
  LEDBrightness();
  }
}

void printLuminosity(){
  lcd.clear();
  lcd.setCursor( 0, 0);
  lcd.print("Current         ");
  lcd.setCursor( 0, 1);
  lcd.print("Luminosity:");
  lcd.print(lighting);
}

void LEDBrightness(){
  Serial.println((255-((lighting/4))));
  analogWrite(LED_GREEN_PIN, (255-((lighting/4))));
}

void measureDistance(){
  unsigned long timeNow = millis();
  if ((timeNow - lastTimeUltraSensor) > ultra_SensorDelay){
    lastTimeUltraSensor += ultra_SensorDelay;
    triggerUltrasonicSensor();
  }
  if (echoFlag){
      echoFlag = false;
      double distanceFromSensor = getUltrasonicDistance();
      if (distanceFromSensor > 10){
        if (distanceFromSensor > 400){
          distanceFromSensor = 400;
        }
        warningBlink(distanceFromSensor); 
        printWarning(distanceFromSensor);
        // Serial.println(distanceFromSensor);  
      }
      else{
        lockLEDs();
      }
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(ECHO_PIN, INPUT);
  pinMode(TRIGGER_PIN, OUTPUT);
  attachInterrupt(digitalPinToInterrupt(ECHO_PIN), echoSensorInterrupt, CHANGE);

  pinMode(LED_YELLOW_PIN, OUTPUT);
  pinMode(LED_RED_PIN, OUTPUT);
  pinMode(LED_GREEN_PIN, OUTPUT);

  pinMode(BUTTON_PIN, INPUT);

  lcd.begin(16,2);
  lcd.clear();
  lcd.print("LOADING.........");
  delay(1000);
  lcd.clear();

  IrReceiver.begin(IR_RECEIVER_PIN);

}

void loop() {
  luminosity();
  // lcdScreen();
  Serial.println(appState);

  if (IrReceiver.decode()) {
    IrReceiver.resume();
    int remotePressed = IrReceiver.decodedIRData.command;
    Serial.println(remotePressed);
    switch (remotePressed){
      case EQ:{
        if (distanceConv == 58.0){
          distanceConv = 58.0 * 2.54;
          distanceType = "in";
        }
        else{
          distanceConv = 58.0;
          distanceType = "cm";
        }
        break;
      }   
      case DOWN:{
        if (appState == 1){
          appState = 3;
        }
        else{
          appState -=1;
        }
        break;
      }   
      case UP:{
        if (appState == 3){
          appState = 1;
        }
        else{
          appState +=1;
        }
        break;
      }   
      case POWER:{
        if (appState == 2){
          defaultSettings();
        }
        break;
      }   
    }
  }

 switch (appState){
    case 1:{
      measureDistance();
      break;
    }
    case 2:{
      lcd.clear();
      lcd.setCursor( 0, 0);
      lcd.print("Press ON/OFF to ");
      lcd.setCursor( 0, 1);
      lcd.print("reset settings  ");
      break;
    }
    case 3:{
      printLuminosity();
      break;
    }
    default:{
      measureDistance();
    }
  }



}