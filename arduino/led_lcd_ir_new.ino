#include <IRremote.h>
#include <LiquidCrystal.h>

#define IR_RECEIVER_PIN 2
#define BUTTON_0 22
#define BUTTON_1 12
#define BUTTON_2 24
#define BUTTON_3 94
#define BUTTON_FUNC_STOP 71

# define LCD_RS_PIN 28
# define LCD_E_PIN 32
# define LCD_D4_PIN 29
# define LCD_D5_PIN 33
# define LCD_D6_PIN 4
# define LCD_D7_PIN 7

#define LED_GREEN 6
#define LED_YELLOW 8
#define LED_RED 10
#define LED_PIN_ARRAY_SIZE 3


LiquidCrystal lcd(LCD_RS_PIN, LCD_E_PIN, LCD_D4_PIN, LCD_D5_PIN, LCD_D6_PIN, LCD_D7_PIN);
byte LEDPinArray[LED_PIN_ARRAY_SIZE] = {LED_GREEN , LED_YELLOW, LED_RED };

bool redOnFlag = false;
bool greenOnFlag = false;
bool yellowOnFlag = false;

unsigned long lastTimeRemotePressed = micros();
unsigned long remoteDelay = 50;

void lightLEDs(int butPressed){
  switch (butPressed){
    case BUTTON_0:{
      for (int i = 0; i < LED_PIN_ARRAY_SIZE ; i++){
        digitalWrite(LEDPinArray[i],LOW);
        redOnFlag = false;
        greenOnFlag = false;
        yellowOnFlag = false;
      }
      break;
    }
    case BUTTON_1:{
      if (!redOnFlag) {
        redOnFlag = true;
        digitalWrite(LED_RED,HIGH);
      }
      else {
        digitalWrite(LED_RED,LOW);
        redOnFlag = false;
      }
      break;
    }
    case BUTTON_2:{
      if (!yellowOnFlag) {
        yellowOnFlag = true;
        digitalWrite(LED_YELLOW,HIGH);
      }
      else {
        digitalWrite(LED_YELLOW,LOW);
        yellowOnFlag = false;
      }
      break;
    }
    case BUTTON_3:{
      if (!greenOnFlag) {
        greenOnFlag = true;
        digitalWrite(LED_GREEN,HIGH);
      }
      else {
        digitalWrite(LED_GREEN,LOW);
        greenOnFlag = false;
      }
      break;
    }     
    // case BUTTON_FUNC_STOP:{
    //   lcd.clear();
    //   break;
    // }       
    // default:{
    //   lcd.clear();
    //   lcd.print("Invalid choice");
    // }       
  }
}

void textForLCD(int butPressed){
  lcd.clear();
  lcd.setCursor(0, 0);
  switch (butPressed){
    case BUTTON_0:{
      lcd.print(butPressed);
      lcd.setCursor(0, 1);
      lcd.print("All LEDs off");
      break;
      }
    case BUTTON_1:{
      lcd.print(butPressed);
      lcd.setCursor(0, 1);
      lcd.print("Toggle LED 1");
      break;
    }
    case BUTTON_2:{
      lcd.print(butPressed);
      lcd.setCursor(0, 1);
      lcd.print("Toggle LED 2");
      break;
    }
    case BUTTON_3:{
      lcd.print(butPressed);
      lcd.setCursor(0, 1);
      lcd.print("Toggle LED 3");
      break;
    }     
    case BUTTON_FUNC_STOP:{
      lcd.clear();
      break;
    }       
    default:{
      lcd.clear();
      lcd.print("Invalid choice");
    }
  }
}


void setup() {
  Serial.begin(115200);
  lcd.begin(16,2);
  lcd.clear();
  for (int i = 0; i < LED_PIN_ARRAY_SIZE ; i++){
    pinMode(LEDPinArray[i],OUTPUT);
  }
  IrReceiver.begin(IR_RECEIVER_PIN);
}

void loop() {
  if (IrReceiver.decode()) {
    IrReceiver.resume();
    int buttonPressed = IrReceiver.decodedIRData.command;
    Serial.println(buttonPressed);
    textForLCD(buttonPressed);
    lightLEDs(buttonPressed);
  } 
}
