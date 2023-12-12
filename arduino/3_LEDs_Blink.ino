#define LED_RED 10
#define LED_YELLOW 8
#define LED_GREEN 6
#define BUTTON_PIN 32

int led_State = 1;

void setup() {
  pinMode(32,INPUT);
  pinMode(6,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(10,OUTPUT);
}

void loop() {
  if (digitalRead(BUTTON_PIN) == LOW){
    if (led_State == 1){
      digitalWrite(LED_RED,HIGH);
      digitalWrite(LED_YELLOW,LOW);
      digitalWrite(LED_GREEN,HIGH);
      led_State = 2;
    }
  else {
      digitalWrite(LED_RED,LOW);
      digitalWrite(LED_YELLOW,HIGH);
      digitalWrite(LED_GREEN,LOW);
      led_State = 1;

    }

  }
  delay(3000);



  // if (digitalRead(BUTTON_PIN) == LOW){
  //   digitalWrite(LED_RED,HIGH);
  //   digitalWrite(LED_YELLOW,LOW);
  //   digitalWrite(LED_GREEN,HIGH);
  //   delay(3000);
  // }
  // if (digitalRead(BUTTON_PIN) == LOW){
  //   digitalWrite(LED_RED,LOW);
  //   digitalWrite(LED_YELLOW,HIGH);
  //   digitalWrite(LED_GREEN,LOW);
  //   delay(3000);
  // }
}
