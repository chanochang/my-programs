#define LED_RED 10
#define LED_YELLOW 8
#define LED_GREEN 6
#define BUTTON_PIN 32

void setup() {
//  Serial.begin(9600);
//  Serial.println("Activate blinker"); 
  pinMode(6,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(10,OUTPUT);
}

void loop() {
  digitalWrite(LED_RED,HIGH);
  digitalWrite(LED_YELLOW,LOW);
  digitalWrite(LED_GREEN,LOW);
  delay(3000);
  digitalWrite(LED_RED,LOW);
  digitalWrite(LED_GREEN,HIGH);
  digitalWrite(LED_YELLOW,LOW);
  delay(3000);
  digitalWrite(LED_RED,LOW);
  digitalWrite(LED_YELLOW,HIGH);
  digitalWrite(LED_GREEN,LOW);
  delay(1000);
}
