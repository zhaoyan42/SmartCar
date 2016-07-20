/*
 Name:		SmartCar.ino
 Created:	2016/7/13 23:21:21
 Author:	赵晏龙
*/

#include <Servo.h>
#include "Car.h"
#include "DistanceDetector.h"


Car car(6, 7, 8, 5, 9, 4);
DistanceDetector distance_detector_high(A0, A1);
DistanceDetector distance_detector_low(A2, A3);
Servo servo;

// the setup function runs once when you press reset or power the board
void setup() {

	Serial.begin(9600);

	car.lunch();

	car.test();

	distance_detector_high.lunch();
	distance_detector_low.lunch();

	servo.attach(10);

}

float get_distance()
{
	float distance = 0;
	distance += distance_detector_high.get_distance();
	distance += distance_detector_high.get_distance();
	distance += distance_detector_high.get_distance();
	return distance / 3.0;
};

long limited_map(long soruce,long soruce_min,long soruce_max,long target_min,long target_max)
{
	if (soruce < soruce_min)soruce = soruce_min;
	if (soruce > soruce_max)soruce = soruce_max;
	return map(soruce, soruce_min, soruce_max, target_min, target_max);
}

// the loop function runs over and over again until power down or reset
void loop() {
	servo.write(90);
	auto middle_high = distance_detector_high.get_distance();
	auto middle_low = distance_detector_low.get_distance();
	auto speed = limited_map((middle_low+ middle_high)/2, 30, 100, 50, 100);
	Serial.println(speed);
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
			car.turn_right(speed);
		}
		else
		{
			car.turn_left(speed);
		}
		delay(500);
	}
	else
	{
		car.forward(speed);
	}
}
