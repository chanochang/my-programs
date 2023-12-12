#define LED_PIN 6

unsigned long newBlinkTime = millis();
unsigned long blinkDelay = 500;
unsigned long presentTime;

int LEDState = LOW;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);

  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  presentTime = millis();
  if (Serial.available() > 0) {
    int data = Serial.parseInt();
    if ((data >= 100) && (data <= 4000)) {
      blinkDelay = data;
    }
  }
  if ((presentTime - newBlinkTime) > blinkDelay){
    if (LEDState == LOW) {
      LEDState = HIGH;
    }
    else {
      LEDState = LOW;
    }
    digitalWrite(LED_PIN, LEDState);
    newBlinkTime += blinkDelay;
  }

}
