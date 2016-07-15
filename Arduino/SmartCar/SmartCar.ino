/*
 Name:		SmartCar.ino
 Created:	2016/7/13 23:21:21
 Author:	赵晏龙
*/

#include "Car.h"
#include "Wheel.h"


Car car(5, 2, 4, 6, 7, 8);

// the setup function runs once when you press reset or power the board
void setup() {

	car.lunch();

}

// the loop function runs over and over again until power down or reset
void loop() {

	car.forward();
	delay(2000);
	car.stop();
	delay(1000);
}
