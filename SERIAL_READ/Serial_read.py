import serial
import time
vref=3.3
bit=4095

def temp(tmp):
    adc=((tmp*vref)/bit)
    tem=(adc*5000*100)/4096
##    tem=float(tmp*0.098)
    return(tem)

ser = serial.Serial(
    port='COM4',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)
name=input("Patient name please:")
name_byt = bytes(name, 'utf-8')
name_byt = name.encode('utf-8')
##name=name.encode()

while 1:
    x=ser.readline().strip()
    time.sleep(.1)
    y=x.decode('ascii').split('.')
    if(len(y)==7):
        t1,t2,t3,t4,t5,t6,t7=y
        out1=temp(int(t1))
        round(out1, 2)
        out2=temp(int(t2))
        round(out2, 2)
        out3=temp(int(t3))
        round(out3, 2)
        out4=temp(int(t4))
        round(out4, 2)
        out5=temp(int(t5))
        round(out5, 2)
        out6=temp(int(t6))
        round(out6, 2)
        out7=temp(int(t7))
        round(out7, 2)
        #fp = open('%s.txt' % name, 'wb')

        filename = "%s.txt" % name_byt
        fp = open(filename , 'a')

        data=str('%.2f : %.2f : %.2f : %.2f : %.2f : %.2f : %.2f \n' %(out1,out2,out3,out4,out5,out6,out7))
        
        data_byt = bytes(data, 'utf-8')
        data_byt = data.encode('utf-8')
    

        
        fp.write(data)
##        fp.write('%.2f  \n' %(out1)
        print('%.2f : %.2f : %.2f : %.2f : %.2f : %.2f : %.2f \n' %(out1,out2,out3,out4,out5,out6,out7))
    else:
        print('Not Enough Data')
        
##    print(y)



