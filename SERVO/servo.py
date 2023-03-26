import RPi                                  ## Import GPIO Library.
import time                                 ## Import ‘time’ library for a delay.

GPIO.setmode(GPIO.BOARD)                    ## Use BOARD pin numbering.
GPIO.setup(22, GPIO.OUT)                    ## set output.

pwm=GPIO.PWM(22,100)                        ## PWM Frequency
pwm.start(0)

angle=160
duty= float(angle)/10 + 2.5

for i in range(duty):
     pwm.ChangeDutyCycle(duty)
     time.sleep(0.1)
time.sleep(1)
GPIO.cleanup()