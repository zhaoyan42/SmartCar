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
const auto servo_right_anlge = 45;
const auto servo_middle_anlge = 90;
const auto servo_left_anlge = 135;
auto is_turning = false;
float right_distance = 0;
float left_distance = 0;

// the setup function runs once when you press reset or power the board
void setup() {

	Serial.begin(9600);

	car.lunch();

	car.test();

	distance_detector_high.lunch();
	distance_detector_low.lunch();

	servo.attach(A5);
	servo.write(servo_middle_anlge);


}

float get_distance()
{
	float distance = 0;
	distance += distance_detector_high.get_distance();
	distance += distance_detector_high.get_distance();
	distance += distance_detector_high.get_distance();
	return distance / 3.0;
};

long limited_map(long soruce, long soruce_min, long soruce_max, long target_min, long target_max)
{
	if (soruce < soruce_min)soruce = soruce_min;
	if (soruce > soruce_max)soruce = soruce_max;
	return map(soruce, soruce_min, soruce_max, target_min, target_max);
}

// the loop function runs over and over again until power down or reset
void loop() {
	auto distance_high = distance_detector_high.get_distance();
	auto distance_low = distance_detector_low.get_distance();
	auto speed = limited_map((distance_low + distance_high) / 2, 30, 100, 50, 100);
	bool too_close = distance_high < 40 || distance_low < 40;
	if (!is_turning && too_close)
	{
		servo.write(servo_right_anlge);
		delay(200);
		right_distance = get_distance();

		servo.write(servo_left_anlge);
		delay(200);
		left_distance = get_distance();

		is_turning = true;
	}
	if (is_turning) {
		if (!too_close)is_turning = false;
		Serial.print(right_distance);
		Serial.print(" ");
		Serial.println(left_distance);
		if (right_distance > left_distance)
		{
			servo.write(servo_left_anlge);
			car.turn_right(speed);
			return;
		}
		else
		{
			servo.write(servo_right_anlge);
			car.turn_left(speed);
			return;
		}
	}
	servo.write(servo_middle_anlge);
	car.forward(speed);
}
