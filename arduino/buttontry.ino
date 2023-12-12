#define BUTTON_PIN 6

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON_PIN, INPUT);
}

void loop() {
  Serial.println(digitalRead(BUTTON_PIN));
  if (digitalRead(BUTTON_PIN) == LOW){
    Serial.println("Button is not pressed");
  } 
  if (digitalRead(BUTTON_PIN) == HIGH){
    Serial.println("Button is  pressed");
  }
  delay(100);
}
