import serial
import time

ser=serial.Serial('COM5')

ser.baudrate=9600
ser.bytesize=8
ser.parity='N'
ser.stopbits=1
data=ser.read()

#dataA=str('a')
#dataB=str('b')
#dataC=str('c')
#dataD=str('d')
def on(a):
   # ser.write(dataA)
   if a  == "led1":
         print "turning on led 1"
         ser.write('a')
   if a  == "led2":
       print "turning on led 2"
       ser.write('c')
    
def off(a):
     if a  == "led1":
         print "turning off led 1"
         ser.write('b')
         
     if a  == "led2":
         print "turning off led 2"
         ser.write('d')


def temp(data):
   while True:
      data=ser.readline()
      print "mere device ka temp h : "+data
      #for i in ser.read():
       #  print i
      
      
     
         
   
   
   # ser.write(dataB)

'''
#while True:
    ser.write(dataA)
    print dataA
    time.sleep(10)
    ser.write(dataB)
    print dataB
    time.sleep(10)


'''
ser.close()
