# include <LiquidCrystal.h>

# define LCD_RS_PIN 28
# define LCD_E_PIN 32
# define LCD_D4_PIN 29
# define LCD_D5_PIN 33
# define LCD_D6_PIN 4
# define LCD_D7_PIN 7

LiquidCrystal lcd(LCD_RS_PIN, LCD_E_PIN, LCD_D4_PIN, LCD_D5_PIN, LCD_D6_PIN, LCD_D7_PIN);

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
  lcd.begin(16,2);
  lcd.print("Hello Benjamin!");
  int row = 0;
}

void loop() {
  if (Serial.available() > 0){
    
  }
}
