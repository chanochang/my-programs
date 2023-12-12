# include <LiquidCrystal.h>

#define ECHO_PIN 3
#define TRIGGER_PIN 11

# define LCD_RS_PIN 28
# define LCD_E_PIN 32
# define LCD_D4_PIN 29
# define LCD_D5_PIN 33
# define LCD_D6_PIN 4
# define LCD_D7_PIN 7

LiquidCrystal lcd(LCD_RS_PIN, LCD_E_PIN, LCD_D4_PIN, LCD_D5_PIN, LCD_D6_PIN, LCD_D7_PIN);

unsigned long lastTimeSensorTriggered = millis();
unsigned long repeatDelay = 60;
volatile unsigned long timeEchoHigh;
volatile unsigned long timeEchoLow;
volatile bool echoFlag = false;

void triggerUltrasonicSensor(){
  digitalWrite(TRIGGER_PIN,LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN,HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN,LOW);
}

double getUltrasonicDistance(){
  double durationMicro = timeEchoLow-timeEchoHigh;
  double distance = durationMicro / 58.0;
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

void printToLCD(double textToPrint){
  String newtextToPrint = String(round(textToPrint));
  for (int i = newtextToPrint.length(); i < 4; i++){
    newtextToPrint += " ";
  }
  lcd.setCursor( 0, 0);
  lcd.print("Rate: ");
  lcd.print(repeatDelay);
  lcd.print( " ms");
  lcd.setCursor( 0, 1);
  lcd.print("Distance: ");
  lcd.print(newtextToPrint);
  lcd.print("cm");
}

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
  pinMode(ECHO_PIN, INPUT);
  pinMode(TRIGGER_PIN, OUTPUT);
  lcd.begin(16,2);
  lcd.clear();
  attachInterrupt(digitalPinToInterrupt(ECHO_PIN), echoSensorInterrupt, CHANGE);

}

void loop() {
  unsigned long timeNow = millis();
  if (timeNow - lastTimeSensorTriggered > repeatDelay){
    lastTimeSensorTriggered +=repeatDelay;
    triggerUltrasonicSensor();
  }
  if (echoFlag){
    echoFlag = false;
    double distanceFromSensor = getUltrasonicDistance();
    if (distanceFromSensor > 400){
      distanceFromSensor = 400;
    }
    Serial.println(distanceFromSensor);
    printToLCD(distanceFromSensor);
  }  
}
