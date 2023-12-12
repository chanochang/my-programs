#define LED_PIN 6
 

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);
  pinMode(LED_PIN,OUTPUT);
  digitalWrite(LED_PIN,LOW);
}

void loop() {
  Serial.println("Enter delay:");
  if (Serial.available() > 0){
    int deltime = Serial.parseInt();
    if ((deltime >= 100) || (deltime <= 1000)){
      digitalWrite(LED_PIN,HIGH);
      delay(deltime);
      digitalWrite(LED_PIN,LOW);
      delay(deltime);
    }
    else{
      Serial.println("Invalid entry, please reenter:");
    }
  }
}
