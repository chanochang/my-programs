void setup() {
  //Set LED pin to output
  Serial.begin(9600);
  Serial.println("Activate blinker"); 
  pinMode(13,OUTPUT);
}

void loop() {
  // Set LED to blink
  digitalWrite(13,HIGH);
  Serial.println("Blinker on");
  delay(2000);
  digitalWrite(13,LOW);
  Serial.println("Blinker off");
  delay(1000);
}
