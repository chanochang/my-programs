#define LED_PIN 6
int stateLED = 1;
int deltime ;

void toggleLED(int delay_time){
  if (stateLED == 1){
    digitalWrite(LED_PIN,HIGH);
    delay(delay_time);
    stateLED = 2;
  }
  if (stateLED == 2){
    digitalWrite(LED_PIN,LOW);
    delay(delay_time);
    stateLED = 1;
  }
}

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);
  pinMode(LED_PIN,OUTPUT);
  digitalWrite(LED_PIN,LOW);
}

void loop() {
  if (Serial.available() > 0){
    deltime = Serial.parseInt();
    }
  if ((deltime >= 100) && (deltime <= 1000)){
    toggleLED(deltime);
  }
  else{
    Serial.println("Invalid entry, please reenter:");
  }
}
