
#define LED_PIN_ARRAY_SIZE 3

#define LED_RED 10
#define LED_YELLOW 8
#define LED_GREEN 6
#define BUTTON_PIN 32

int led_State = 1;
byte LEDPinArray[LED_PIN_ARRAY_SIZE] = {LED_RED, LED_YELLOW, LED_GREEN};

void setLEDPinModes() {
  for (int i = 0; i< LED_PIN_ARRAY_SIZE; i++){
    pinMode(LEDPinArray[i],OUTPUT);
  }
}

void turnOffAllLEDs() {
  for (int i = 0; i< LED_PIN_ARRAY_SIZE; i++){
      digitalWrite(LEDPinArray[i],LOW);
  }
}

void toggleLEDs() {
  if (led_State == 1){
    digitalWrite(LED_RED,HIGH);
    digitalWrite(LED_YELLOW,LOW);
    digitalWrite(LED_GREEN,HIGH);
    led_State = 2;
  }
else {
    digitalWrite(LED_RED,LOW);
    digitalWrite(LED_YELLOW,HIGH);
    digitalWrite(LED_GREEN,LOW);
    led_State = 1;
  }
}

void setup() {
  pinMode(32,INPUT);
  setLEDPinModes();
  turnOffAllLEDs();
}

void loop() {
  if (digitalRead(BUTTON_PIN) == LOW){
    toggleLEDs();
  delay(300);
  }
}
