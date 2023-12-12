void setup() {
  //Set LED pin to output
  Serial.begin(9600);
  Serial.println("Activate blinker"); 
  pinMode(12,OUTPUT);
}

void loop() {
  // Set LED to blink
  digitalWrite(12,HIGH);
  Serial.println("Blinker on");
  delay(2000);
  digitalWrite(12,LOW);
  Serial.println("Blinker off");
  delay(2000);
}
