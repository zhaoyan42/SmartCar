// DistanceDetect.h

#ifndef _DISTANCEDETECT_h
#define _DISTANCEDETECT_h

#if defined(ARDUINO) && ARDUINO >= 100
	#include "arduino.h"
#else
	#include "WProgram.h"
#endif

class DistanceDetector
{
 protected:
	 int trigger_pin, echo_pin;
	 
	 void send_signal()
	 {
		 digitalWrite(trigger_pin, LOW);
		 delayMicroseconds(2);
		 digitalWrite(trigger_pin, HIGH);
		 delayMicroseconds(10);
		 digitalWrite(trigger_pin, LOW);
	 }

	 int receive_signal()
	 {
		 return pulseIn(echo_pin, HIGH);
	 }

 public:
	DistanceDetector(int trigger_pin, int echo_pin)
		: trigger_pin(trigger_pin),
		  echo_pin(echo_pin)
	{
	}

	/// return unit is cm
	float get_distance()
	{
		send_signal();
		return receive_signal() / 58.00;
	}

};

#endif

