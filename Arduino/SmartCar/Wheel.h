// Wheel.h

#ifndef _WHEEL_h
#define _WHEEL_h

#if defined(ARDUINO) && ARDUINO >= 100
	#include "arduino.h"
#else
	#include "WProgram.h"
#endif

class WheelClass
{
 protected:


 public:
	void init();
};

extern WheelClass Wheel;

#endif

