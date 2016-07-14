/*
 Name:		SmartCar.ino
 Created:	2016/7/13 23:21:21
 Author:	赵晏龙
*/

#include "Wheel.h"
int in1_pin, in2_pin;

// the setup function runs once when you press reset or power the board
void setup() {
	in1_pin = 5;
	in2_pin = 6;
	pinMode(in1_pin, OUTPUT);
	pinMode(in2_pin, OUTPUT);
	digitalWrite(in1_pin, HIGH);
	digitalWrite(in2_pin, LOW);
}

// the loop function runs over and over again until power down or reset
void loop() {

}
