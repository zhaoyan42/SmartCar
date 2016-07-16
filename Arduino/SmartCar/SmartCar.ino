/*
 Name:		SmartCar.ino
 Created:	2016/7/13 23:21:21
 Author:	赵晏龙
*/

#include "Car.h"


Car car(6, 7, 8, 5, 2, 4);

// the setup function runs once when you press reset or power the board
void setup() {

	car.lunch();

	car.test();

	car.forward();
	delay(1000);
	car.backward();
	delay(1000);
	car.turn_left();
	delay(1000);
	car.turn_right();
	delay(1000);
	car.stop();
}

// the loop function runs over and over again until power down or reset
void loop() {
}
