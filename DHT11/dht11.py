import RPi.GPIO as GPIO
import time
import dht11

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,0)
t1 = dht11.DHT11(pin=3)

def dht1():
    t1_Result = t1.read()
    if t1_Result.is_valid():
        temp1 = str(t1_Result.temperature)    

        hum = str(t1_Result.humidity)
        print temp1,hum

while 1:
    dht1()
