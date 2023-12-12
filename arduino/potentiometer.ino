#define POTENTIOMETER A15

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(analogRead(POTENTIOMETER));
  delay(100);
}
