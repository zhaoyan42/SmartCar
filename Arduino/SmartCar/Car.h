// Car.h

#ifndef _CAR_h
#define _CAR_h

#if defined(ARDUINO) && ARDUINO >= 100
#include "arduino.h"
#else
#include "WProgram.h"
#endif
#include "Wheel.h"

class Car
{
protected:
	Wheel *wheel1, *wheel2;

public:
	Car(int en1, int in1_1, int in1_2, int en2, int in2_1, int in2_2)
	{
		this->wheel1 = new Wheel(en1, in1_1, in1_2);
		this->wheel2 = new Wheel(en2, in2_1, in2_2);
	}

	void lunch()
	{
		this->wheel1->lunch();
		this->wheel2->lunch();
	}

	void forward()
	{
		this->wheel1->run();
		this->wheel2->run();
	}

	void stop()
	{
		this->wheel1->stop();
		this->wheel2->stop();
	}
};

#endif

