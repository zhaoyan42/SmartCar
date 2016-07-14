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

	void lunch()
	{
		pinMode(enable_pin, OUTPUT);
		pinMode(in1_pin, OUTPUT);
		pinMode(in2_pin, OUTPUT);
	}

	void run()
	{
		analogWrite(enable_pin, 255);
		digitalWrite(in1_pin, HIGH);
		digitalWrite(in2_pin, LOW);
	}

	void stop()
	{
		analogWrite(enable_pin, 0);
	}
};

#endif

