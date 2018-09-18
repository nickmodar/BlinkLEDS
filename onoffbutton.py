import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

pin = 4
#white
pin1 = 5
#Green
pin2 = 26
#Red
pin3= 13
#Green
pin4= 19
#yellow


counter = 0

while True:
    if not GPIO.input(22):
        counter = counter + 1
        print(counter)
        
        if counter == 1:
          
            GPIO.output(pin, GPIO.HIGH)
            GPIO.output(pin1, GPIO.HIGH)
            GPIO.output(pin2, GPIO.LOW)
            GPIO.output(pin3, GPIO.LOW)
            GPIO.output(pin4, GPIO.LOW)
            
        if counter == 2:
           
            GPIO.output(pin, GPIO.LOW)
            GPIO.output(pin1, GPIO.HIGH)
            GPIO.output(pin2, GPIO.HIGH)
            GPIO.output(pin3, GPIO.LOW)
            GPIO.output(pin4, GPIO.LOW)
            
        if counter == 3:
           
            GPIO.output(pin, GPIO.HIGH)
            GPIO.output(pin1, GPIO.LOW)
            GPIO.output(pin2, GPIO.HIGH)
            GPIO.output(pin3, GPIO.LOW)
            GPIO.output(pin4, GPIO.LOW)
            
        if counter == 4:
            GPIO.output(pin, GPIO.LOW)
            GPIO.output(pin1, GPIO.LOW)
            GPIO.output(pin2, GPIO.LOW)
            GPIO.output(pin3, GPIO.HIGH)
            GPIO.output(pin4, GPIO.HIGH)
        
        if counter == 5:
            GPIO.output(pin, GPIO.LOW)
            GPIO.output(pin1, GPIO.LOW)
            GPIO.output(pin2,GPIO.LOW)
            GPIO.output(pin3, GPIO.HIGH)
            GPIO.output(pin4, GPIO.HIGH)
        
            counter = 0
            
        while not GPIO.input(22):
            pass
        
            
            
            
            
        
    
