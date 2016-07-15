// Wheel.h

#ifndef _WHEEL_h
#define _WHEEL_h

#if defined(ARDUINO) && ARDUINO >= 100
#include "arduino.h"
#else
#include "WProgram.h"
#endif


class Wheel
{
private:
	int enable_pin, in1_pin, in2_pin;

protected:

public:
	
	Wheel(int enable_pin, int in1_pin, int in2_pin)
	{
		this->enable_pin = enable_pin;
		this->in1_pin = in1_pin;
		this->in2_pin = in2_pin;
	}
	
	enum WheelDirection
	{
		Positive,
		Negative
	};

	String get_wheel_direction_name(WheelDirection wheel_direction)
	{
		switch (wheel_direction)
		{
		case Positive:
			return "Positive";

		case Negative:
			return "Negative";
		}
	}

	void lunch()
	{
		pinMode(enable_pin, OUTPUT);
		pinMode(in1_pin, OUTPUT);
		pinMode(in2_pin, OUTPUT);
	}

	void speed(int speed = 100)
	{
		analogWrite(enable_pin, map(speed, 0, 100, 0, 255));
	}

	void rotate_direction(WheelDirection wheel_direction)
	{
		switch (wheel_direction)
		{
		case Positive:
			digitalWrite(in1_pin, HIGH);
			digitalWrite(in2_pin, LOW);
			break;

		case Negative:
			digitalWrite(in1_pin, LOW);
			digitalWrite(in2_pin, HIGH);
			break;

		default:
			throw "Unsupported Direction" + get_wheel_direction_name(wheel_direction);
		}
	}

	void stop()
	{
		speed(0);
	}
};

#endif

