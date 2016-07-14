/*
 Name:		SmartCar.ino
 Created:	2016/7/13 23:21:21
 Author:	赵晏龙
*/

#include "Wheel.h"

Wheel wheel1(5, 2, 4);
Wheel wheel2(6, 7, 8);

// the setup function runs once when you press reset or power the board
void setup() {

	wheel1.lunch();
	wheel2.lunch();

}

// the loop function runs over and over again until power down or reset
void loop() {

	wheel1.run();
	wheel2.run();
	delay(2000);
	wheel1.stop();
	wheel2.stop();
	delay(1000);
}
