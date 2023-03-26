from Adafruit_PWM_Servo_Driver import PWM
import math
import subprocess
import serial

##arm=serial.Serial('/dev/ttyUSB0',9600,timeout=.1)

pwm = PWM(0x40)

# Constants defining the range of the servo
SERVO_MIN = 150
SERVO_MAX = 600
HALF_PI = math.pi / 2.0
MIDPOINT = 375.0
SPAN = 225.0


b=2
fb=3
ud=4
p=5


def init():
    pwm.setPWMFreq(60)
##    pwm.setPWM(b, 0, 375)
##    pwm.setPWM(fb, 0, 375)
##    pwm.setPWM(ud, 0, 375)
    pwm.setPWM(p, 0, 375)

while(1):
    init()



arm_ud=375
arm_fb=375
arm_b=375
arm_flag=0
arm_p=375
def cntl():
    global arm_ud,arm_fb,arm_b,arm_p,arm_flag
    while(1):
        a=arm.readline()
        #print a
        if 'f' in a:
            print ('fwd')
        if 'b' in a:
            print ('bck')
        if 'l' in a:
            print ('left')
        if 'r' in a:
            print ('right')
        if 's' in a:
            print ('stop')
        if 'a' in a:
            print ('pick')
            arm_fl(arm_flag)
            if arm_flag==1:
                arm_p=375
            if arm_flag==2:
                arm_p=550
                arm_flag=0
        if '#' in a:
            if '*' in a:
                data=a[a.index('#')+1:a.index('*')]
                print (data)
                data=data.split(',')
                arm_ud=int(data[0])
                arm_fb=int(data[1])
                arm_b=int(data[2])
        
        pwm.setPWM(b, 0, arm_b)
        pwm.setPWM(fb, 0, arm_fb)
        pwm.setPWM(ud, 0, arm_ud)
        pwm.setPWM(p, 0, arm_p)
        






##cntl()








    
    
