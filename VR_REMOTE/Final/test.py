from flask import Flask
from Adafruit_PWM_Servo_Driver import PWM
import math
import subprocess
import RPi.GPIO as g
import time
import serial
import _thread




app = Flask(__name__)

pwm = PWM(0x40)

arm=serial.Serial('/dev/ttyUSB0',9600,timeout=0.1)

# Constants defining the range of the servo
SERVO_MIN = 150
SERVO_MAX = 600
HALF_PI = math.pi / 2.0
MIDPOINT = 375.0
SPAN = 225.0

MIDPOINT1 = 150.0
SPAN1 = 225.0

# channels
PAN = 1
TILT = 0
b=2
fb=3
ud=4
p=5
led_G = 8
led_R = 10

g.setmode(g.BOARD)
g.setwarnings(False)
g.setup(37,0)
g.setup(35,0)
g.setup(33,0)
g.setup(31,0)
g.setup(led_G,0)
g.setup(led_R,0)

g.setup(40,1,pull_up_down=g.PUD_UP)
g.setup(38,1,pull_up_down=g.PUD_DOWN)
g.setup(36,1,pull_up_down=g.PUD_DOWN)

g.output(37,0)
g.output(35,0)
g.output(33,0)
g.output(31,0)

time.sleep(3)
g.output(led_G,0)
g.output(led_R,0)


def fwd():
    g.output(35,1)
    g.output(37,0)
    g.output(33,0)
    g.output(31,1) 
    
   
    
def stop():
    g.output(35,0)
    g.output(37,0)
    g.output(33,0)
    g.output(31,0)
    
   

def rev():
    g.output(35,0)
    g.output(37,1)
    g.output(33,1)
    g.output(31,0)
    
    
    

def left():
    g.output(35,1)
    g.output(37,0)
    g.output(33,0)
    g.output(31,0)
   

def right():
    g.output(35,0)
    g.output(37,0)
    g.output(33,0)
    g.output(31,1)
   
    



def init():
    pwm.setPWMFreq(60)
    pwm.setPWM(TILT, 0, 375)
    pwm.setPWM(b, 0, 1000)
    pwm.setPWM(fb, 0, 600)
    pwm.setPWM(ud, 0, 375)
    pwm.setPWM(p, 0, 375)




arm_ud=400
arm_fb=375
arm_b=375
arm_flag=0
arm_Rot_flag=0
arm_p=375

def cntl():
    global arm_ud,arm_fb,arm_b,arm_p,arm_flag,arm_Rot_flag
    
    while(1):
        a=arm.readline()
        a=a.decode(encoding='UTF-8',errors='strict')
        if a is None:
            stop()
            
        print(a)
        if 'f' in a:
            print ('fwd')
            fwd()
        if 'b' in a:
            print ('bck')
            rev()
        if 'l' in a:
            print ('left')
            left()
        if 'r' in a:
            print ('right')
            right()
        if 's' in a:
            print ('stop')
            stop()
        if 'ot' in a:
            print("available")
            
            arm_Rot_flag = arm_Rot_flag + 1
            print("arm_Rot_flag ",arm_Rot_flag)
        
            if(arm_Rot_flag == 1):
                print("inside 1")
##                time.sleep(2)
                arm_ud = 400
            if(arm_Rot_flag == 2):
                arm_ud = 610
                print("inside 2")
##                time.sleep(2)
                arm_Rot_flag=0
                
        if 'a' in a:
            print ('pick')
            arm_flag=arm_flag+1
            print( arm_flag)
            if arm_flag==1:
                arm_p=330
            if arm_flag==2:
                arm_p=490
                arm_flag=0
        if '#' in a:
            if '*' in a:
                data=a[a.index('#')+1:a.index('*')]
##                print (data)
                data=data.split(',')
                
##                arm_ud=int(data[0])
##                print("arm_ud", arm_ud)
                
                arm_fb=int(data[1])
                print("arm_fb", arm_fb)
                
                arm_b=int(data[2])
                print("arm_b", arm_b)
        
        
        pwm.setPWM(b, 0, arm_b)
        pwm.setPWM(fb, 0, arm_fb)
        pwm.setPWM(4, 0, arm_ud)
        pwm.setPWM(p, 0, arm_p)
        




@app.route('/')
def hello():
    return "hello"


def normalize(num):
    '''
    num: a float between -PI and PI.
    returns: num normalized between SERVO_MIN and SERVO_MAX.
    '''
    return int(MIDPOINT + ((num / HALF_PI) * SPAN))
def normalize1(num1):
    '''
    num: a float between -PI and PI.
    returns: num normalized between SERVO_MIN and SERVO_MAX.
    '''
    return int(MIDPOINT1 + ((num1 / HALF_PI) * SPAN1))


@app.route("/move/<pitch>/<yaw>")
def move(pitch, yaw):
    pwm.setPWM(TILT, 0, normalize1(-float(pitch)))
    pwm.setPWM(PAN, 0, normalize(float(yaw)))
    return "OK"

##init()
##cntl()

try:
    init()
    _thread.start_new_thread(cntl,())
    app.run(host='192.168.43.4', port=8080, debug=True, use_reloader=False)


except:
    print ('err')
    pass


while 1:
   pass

