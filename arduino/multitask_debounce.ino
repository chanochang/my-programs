#define POTENTIOMETER A15 
#define BUTTON_PIN 32

#define LED_PIN_1 10
#define LED_PIN_2 8
#define LED_PIN_3 6



unsigned long newBlinkTime = millis();
unsigned long newButtonTime = millis();
unsigned long blinkDelay = 1000;
unsigned long debounceDelay = 40;
unsigned long presentTime;

int LEDState = LOW;
byte ButtonState = 1;
int toggleLEDState = 1;



void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
  pinMode(BUTTON_PIN, INPUT);

  pinMode(LED_PIN_1, OUTPUT);
  pinMode(LED_PIN_2, OUTPUT);
  pinMode(LED_PIN_3, OUTPUT);
  digitalWrite(LED_PIN_2, LOW );
  digitalWrite(LED_PIN_3, HIGH);

}

void loop() {
    //Blink pin at constant rate
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

  //toggle leds with button, first debounce button
  presentTime = millis();

  if ((presentTime - newButtonTime) > debounceDelay){
    byte newButtonState = digitalRead(BUTTON_PIN);
    if (newButtonState != ButtonState){
     if (newButtonState == HIGH) {
          if (toggleLEDState == 1){
            digitalWrite(LED_PIN_2, LOW);
            digitalWrite(LED_PIN_3, HIGH);
            toggleLEDState = 2;
          }
          else{
            digitalWrite(LED_PIN_2, HIGH);
            digitalWrite(LED_PIN_3, LOW);
            toggleLEDState = 1;
          }
      }
    ButtonState = newButtonState;
    newButtonTime = presentTime;
    }
  }
}
