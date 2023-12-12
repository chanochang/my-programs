#define POTENTIOMETER A12?
#define LED_PIN 10

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN,OUTPUT);
}

void loop() {
  Serial.println(analogRead(POTENTIOMETER));
  analogWrite(LED_PIN, (analogRead(POTENTIOMETER)/4));
}
