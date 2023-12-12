#define ECHO_PIN 3
#define TRIGGER_PIN 11

unsigned long lastTimeSensorTriggered = millis();
unsigned long repeatDelay = 100;

void triggerUltrasonicSensor(){
  digitalWrite(TRIGGER_PIN,LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN,HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN,LOW);
}

double getUltrasonicDistance(){
  unsigned long timeStartPulse = micros();
  double durationMicro = pulseIn(ECHO_PIN, HIGH);
  unsigned long timeEndPulse = micros();
  Serial.println(timeEndPulse-timeStartPulse);
  double distance = durationMicro / 58.0;
  return distance;
}
void setup() {
  Serial.begin(115200);
  pinMode(ECHO_PIN, INPUT);
  pinMode(TRIGGER_PIN, OUTPUT);
}

void loop() {
  unsigned long timeNow = millis();
  if (timeNow - lastTimeSensorTriggered > repeatDelay){
  lastTimeSensorTriggered +=repeatDelay;
  triggerUltrasonicSensor();
  Serial.println(getUltrasonicDistance());
  }
}
