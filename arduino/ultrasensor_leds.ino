#define ECHO_PIN 3
#define TRIGGER_PIN 11
#define LED_GREEN 6
#define LED_YELLOW 8
#define LED_RED 10

unsigned long lastTimeSensorTriggered = millis();
unsigned long repeatDelay = 100;
volatile unsigned long timeEchoHigh;
volatile unsigned long timeEchoLow;
volatile bool echoFlag = false;

void triggerUltrasonicSensor(){
  digitalWrite(TRIGGER_PIN,LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN,HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN,LOW);
}

double getUltrasonicDistance(){
  // unsigned long timeStartPulse = micros();
  // double durationMicro = pulseIn(ECHO_PIN, HIGH);
  // unsigned long timeEndPulse = micros();
  double durationMicro = timeEchoLow-timeEchoHigh;
  //Serial.println(durationMicro);
  double distance = durationMicro / 58.0;
  return distance;
}

void lightLEDs(double distFromSensor){  
    if (distFromSensor >= 100){
      digitalWrite(LED_GREEN, HIGH);
      digitalWrite(LED_YELLOW, LOW);
      digitalWrite(LED_RED, LOW);
    }
    else if ((distFromSensor >=15)) {
      digitalWrite(LED_GREEN, LOW);
      digitalWrite(LED_YELLOW, HIGH);
      digitalWrite(LED_RED, LOW);
    }    
    else {
      digitalWrite(LED_GREEN, LOW);
      digitalWrite(LED_YELLOW, LOW);
      digitalWrite(LED_RED, HIGH);
    }
}

void echoSensorInterrupt(){
  if (digitalRead(ECHO_PIN) == HIGH){
    timeEchoHigh = micros();
  }
  else {
    timeEchoLow = micros();
    echoFlag = true;
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(ECHO_PIN, INPUT);
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_RED, OUTPUT);

  digitalWrite(LED_GREEN,LOW);
  digitalWrite(LED_YELLOW,LOW);
  digitalWrite(LED_RED,LOW);
  attachInterrupt(digitalPinToInterrupt(ECHO_PIN), echoSensorInterrupt, CHANGE);
}

void loop() {
  unsigned long timeNow = millis();
  if (timeNow - lastTimeSensorTriggered > repeatDelay){
    lastTimeSensorTriggered +=repeatDelay;
    triggerUltrasonicSensor();
  }
  if (echoFlag){
    echoFlag = false;
    double distanceFromSensor = getUltrasonicDistance();
    lightLEDs(distanceFromSensor);
    Serial.println(distanceFromSensor);
  } 
}
