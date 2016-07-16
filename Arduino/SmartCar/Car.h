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
private:
	Car(Wheel* wheel_left, Wheel* wheel_right)
		: wheel_left(wheel_left),
		wheel_right(wheel_right)
	{
	}

protected:
	Wheel *wheel_left, *wheel_right;

public:
	Car(int left_en, int left_in1, int left_in2, int right_en, int right_in1, int right_in2)
		:Car(new Wheel(left_en, left_in1, left_in2), new Wheel(right_en, right_in1, right_in2))
	{
	}

	~Car()
	{
		delete this->wheel_left;
		delete this->wheel_right;
	}

	void lunch()
	{
		this->wheel_left->lunch();
		this->wheel_right->lunch();
	}

	void test()
	{

		this->wheel_left
			->rotate_direction(Wheel::Positive)
			->speed(100);
		delay(500);
		this->wheel_left
			->rotate_direction(Wheel::Negative)
			->speed(100);
		delay(500);
		this->wheel_left->stop();

		this->wheel_right
			->rotate_direction(Wheel::Positive)
			->speed(100);
		delay(500);
		this->wheel_right
			->rotate_direction(Wheel::Negative)
			->speed(100);
		delay(500);
		this->wheel_right->stop();
	}

	void forward()
	{
		this->wheel_left
			->rotate_direction(Wheel::Positive)
			->speed(70);
		this->wheel_right
			->rotate_direction(Wheel::Positive)
			->speed(70);
	}

	void backward()
	{
		this->wheel_left
			->rotate_direction(Wheel::Negative)
			->speed(70);
		this->wheel_right
			->rotate_direction(Wheel::Negative)
			->speed(70);
	}

	void turn_left()
	{
		this->wheel_left
			->rotate_direction(Wheel::Negative)
			->speed(70);
		this->wheel_right
			->rotate_direction(Wheel::Positive)
			->speed(70);
	}

	void turn_right()
	{
		this->wheel_left
			->rotate_direction(Wheel::Positive)
			->speed(70);
		this->wheel_right
			->rotate_direction(Wheel::Negative)
			->speed(70);
	}

	void stop()
	{
		this->wheel_left->stop();
		this->wheel_right->stop();
	}
};

#endif

