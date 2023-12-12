#define PHOTORESISTOR A12
#define LED_RED_PIN 10
#define LED_GREEN_PIN 6

void setup() {
  Serial.begin(115200);
  pinMode(LED_RED_PIN,OUTPUT);
  pinMode(LED_GREEN_PIN,OUTPUT);
}

void loop() {
  if ((analogRead(PHOTORESISTOR)) > (1023/3)){
    digitalWrite(LED_RED_PIN, LOW);
  }
  else {
    digitalWrite(LED_RED_PIN, HIGH);
  }    
  analogWrite(LED_GREEN_PIN, (255-((analogRead(PHOTORESISTOR))/4)));
}
