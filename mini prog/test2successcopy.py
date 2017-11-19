import socket

import select

import RPi.GPIO as GPIO

import time

pin=7

pin1=29

GPIO.setwarnings(False)

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin,GPIO.OUT)

GPIO.setup(pin1,GPIO.OUT)

data='5'

port=12345


try:
                

        
s=socket.socket()
        
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        
s.bind(("192.168.1.3",port))
        
s.listen(5)

        
while True:
                
print("waiting for client.....")
               
 c,addr = s.accept()
                
print('Connected to',addr)
               
 c.send('Raspberry connected')
               
 while True:
                        
data=c.recv(8)
                        
print(data)
                        
if data=='led1on':
                                
GPIO.output(pin,GPIO.HIGH)
                        
if data=='led1off':
                               
 GPIO.output(pin,GPIO.LOW)
                                
time.sleep(2)
                        
if data=='led2on':
                                
GPIO.output(pin1,GPIO.HIGH)
                        
if data=='led2off':
                               
 GPIO.output(pin1,GPIO.LOW)
                                
time.sleep(2)
                        
if data=='exitmango':
                                
c.shutdown(2)
                                
c.close()
                                
s.shutdown(2)
                                
s.close()
                                
print("closed all socket successful and MANGO shutting down")
                                
exit(0)
                                
                        
data='0'
                        
if data=='0':
                                
break
                
c.shutdown(2)
                
c.close()
        
s.shutdown(2)
        
s.close()
        

except Exception, e:
        print(e)
        print("socket closing")
        print("closing GPIO")
        GPIO.cleanup()
        s.shutdown(2)
        s.close()
