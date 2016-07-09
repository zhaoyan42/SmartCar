import RPi.GPIO as GPIO
import time
import car

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

car = car.Car4Wheel([24,25,18,23,12,16,20,21],GPIO.LOW)

car.lunch()

car.test()



from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if request.form["direction"] == "forward":
            car.forward()
        elif request.form["direction"] == "backward":
            car.backward()
        else:
            car.stop()
    return render_template('./UI.html')
       
       

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8888)





car.stop()
car.terminate()

GPIO.cleanup()

