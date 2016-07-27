#include <TimerOne.h>
#include <PID_v1.h>
#include "Car.h"


double right_count, left_count, adjusted_left_value = 100, adjusted_right_value = 100, t_left_count=0,t_right_count=0;


//PID left_pid(&left_count, &adjusted_left_value, &right_count, 1, 10, 0.1, DIRECT);
PID right_pid(&right_count, &adjusted_right_value, &left_count, 1, 10, 0.1, DIRECT);
Car car(6, 7, 8, 5, 9, 4);




void count_left()
{
	t_left_count++;
};

void count_right()
{
	t_right_count++;
};

void reset_counter()
{
	right_count = t_right_count;
	t_right_count = 0;
	left_count = t_left_count;
	t_left_count = 0;
//	left_pid.Compute();
	right_pid.Compute();

	Serial.print(right_count);
	Serial.print(" ");
	Serial.print(left_count);
	Serial.print(" ");
	Serial.print(adjusted_right_value);
	Serial.print(" ");
	Serial.println(adjusted_left_value);
}

void setup()
{
	Serial.begin(9600);

	left_count = 0;
	right_count = 1000;

//	left_pid.SetMode(AUTOMATIC);
//	left_pid.SetOutputLimits(0, 100);
	right_pid.SetMode(AUTOMATIC);
	right_pid.SetOutputLimits(0, 100);


	attachInterrupt(0, count_right, FALLING);
	attachInterrupt(1, count_left, FALLING);

	Timer1.initialize(100000); // initialize timer1 and set interrupt period
	Timer1.attachInterrupt(reset_counter);

	car.lunch();
	
	car.forward();

	delay(100);
}

void loop()
{
	car.forward(adjusted_left_value,adjusted_right_value);
}