#include "Arduino.h"
#include <LiquidCrystal.h>
#include "constants.h"
#include "utils.h"


//////////////////////////////////
// GLOBALS
//////////////////////////////////

// select the pins used on the LCD panel
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

void setup() {
	//init serial monitor
	Serial.begin(9600);
	Serial.println("Setup fun");

	//init lcd
	lcd.begin(LCD_CHARS, LCD_LINES);        
	pinMode(LCD_CTRL_LIGHT_PIN, OUTPUT);
	analogWrite(LCD_CTRL_LIGHT_PIN, DEFAULT_LCD_LIGHT);
	lcdPrintLine(lcd, 0, "line 1");
	lcdPrintLine(lcd, 1, "line 2");
}


void loop() {
	Serial.println("loop");
	delay(LOOP_WAITING);
}