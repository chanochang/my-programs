#define POTENTIOMETER A15 
#define BUTTON_PIN 32

#define LED_PIN_1 10
#define LED_PIN_2 8
#define LED_PIN_3 6



unsigned long newBlinkTime = millis();
unsigned long blinkDelay = 500;
unsigned long presentTime;

int LEDState = LOW;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
  pinMode(BUTTON_PIN, INPUT);

  pinMode(LED_PIN_1, OUTPUT);
  pinMode(LED_PIN_2, OUTPUT);
  pinMode(LED_PIN_3, OUTPUT);
}

void loop() {
  presentTime = millis();
  if (Serial.available() > 0) {
    int data = Serial.parseInt();
    if ((data >= 100) && (data <= 4000)) {
      blinkDelay = data;
    }
  }

  //Blink pin at inputted rate
  presentTime = millis();
  if ((presentTime - newBlinkTime) > blinkDelay){
    if (LEDState == LOW) {
      LEDState = HIGH;
    }
    else {
      LEDState = LOW;
    }
    digitalWrite(LED_PIN_1, LEDState);
    newBlinkTime += blinkDelay;
  }

  //Adjust pin brightness using potentiometer
  Serial.println(analogRead(POTENTIOMETER));
  analogWrite(LED_PIN_2, analogRead((POTENTIOMETER)/4));

  //Blink pin when button is pressed
  if (digitalRead(BUTTON_PIN) == HIGH){
    digitalWrite(LED_PIN_3, HIGH);
  } 
  else {
    digitalWrite(LED_PIN_3, LOW);
  }
}
