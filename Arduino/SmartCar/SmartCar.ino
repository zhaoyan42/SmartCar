/*
 Name:		SmartCar.ino
 Created:	2016/7/13 23:21:21
 Author:	赵晏龙
*/

#include <Servo.h>
#include "Car.h"
#include "DistanceDetector.h"


Car car(6, 7, 8, 5, 2, 4);
DistanceDetector distance_detector_high(13, 12);
DistanceDetector distance_detector_low(10, 11);
Servo servo;

// the setup function runs once when you press reset or power the board
void setup() {

	Serial.begin(9600);

	car.lunch();

	car.test();

	distance_detector_high.lunch();
	distance_detector_low.lunch();

	servo.attach(3);

}

float get_distance()
{
	float distance = 0;
	distance += distance_detector_high.get_distance();
	distance += distance_detector_high.get_distance();
	distance += distance_detector_high.get_distance();
	return distance / 3.0;
};

// the loop function runs over and over again until power down or reset
void loop() {
	servo.write(90);
	auto middle_high = distance_detector_high.get_distance();
	auto middle_low = distance_detector_low.get_distance();
	if (middle_high < 40 || middle_low <40)
	{
		car.stop();

		servo.write(45);
		delay(200);
		float right_distance = get_distance();

		servo.write(135);
		delay(200);
		float left_distance = get_distance();
		
		servo.write(90);

		if(right_distance>left_distance)
		{
			car.turn_right();
		}
		else
		{
			car.turn_left();
		}
		delay(500);
	}
	else
	{
		car.forward();
	}
}
