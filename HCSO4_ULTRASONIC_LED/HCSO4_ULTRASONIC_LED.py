import matplotlib
import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
 
TRIG = 23
ECHO = 24
 
print "Distance measurement in progress"
 
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
 
fig = plt.figure()
plt.xlim([-400, 400])
plt.ylim([-400, 400])
 
 
while True:
 
 
  GPIO.output(TRIG, False)
  print "Waitng For Sensor To Settle"
  time.sleep(2)
 
  GPIO.output(TRIG, True)
  time.sleep(0.00001)                     
  GPIO.output(TRIG, False)                
 
  while GPIO.input(ECHO)==0:              
    pulse_start = time.time()             
 
  while GPIO.input(ECHO)==1:              
    pulse_end = time.time()               
 
  pulse_duration = pulse_end - pulse_start
 
  distance = pulse_duration * 17150        
 
  distance = round(distance, 2)           
 
  if distance < 100:     
    print "Distance:",distance - 0.5,"cm" 
 
    ax = fig.add_subplot(111)
    rect1 = matplotlib.patches.Rectangle((-200,-100), 400, 200, color='red')
    ax.add_patch(rect1)
    plt.draw()
    plt.pause(0.00001)
 
  if distance > 100 and distance < 200:     
    print "Distance:",distance - 0.5,"cm" 
    ax = fig.add_subplot(111)
    rect1 = matplotlib.patches.Rectangle((-200,-100), 400, 200, color='yellow')
    ax.add_patch(rect1)
    plt.draw()
    plt.pause(0.00001)
   
  if distance > 200:
    print "Out Of Range"                  
    ax = fig.add_subplot(111)
    rect1 = matplotlib.patches.Rectangle((-200,-100), 400, 200, color='green')
    ax.add_patch(rect1)
    plt.draw()
    plt.pause(0.00001)