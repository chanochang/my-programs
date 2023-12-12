#define BUTTON_PIN 6

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON_PIN, INPUT);
}

void loop() {
  Serial.println(digitalRead(BUTTON_PIN));
  delay(100);
}
