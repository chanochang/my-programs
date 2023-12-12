#include <EEPROM.h>

#define POTENTIOMETER A15 
#define LED_PIN 10

int maxBrightness = 1023/4;
byte brightnessFromMem;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN,OUTPUT);
  brightnessFromMem = EEPROM.read(240);
  if (brightnessFromMem ==0){
    brightnessFromMem = 255;
  }

}

void loop() {
  if (Serial.available()>0){
    int data = Serial.parseInt();
    maxBrightness = data;
    EEPROM.write(240,maxBrightness);
  }
  int val_Potentiometer = analogRead(POTENTIOMETER);   
  int LED_Brightness = (val_Potentiometer/4);
  if (LED_Brightness > maxBrightness){
    LED_Brightness = maxBrightness;
  }
  analogWrite(LED_PIN, LED_Brightness);
}