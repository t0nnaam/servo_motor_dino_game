from kiddeemata import kiddeemata, OUTPUT, INPUT
import sys
import time
from tkinter import *
from datetime import datetime

board = kiddeemata.KiddeeMata()
board.set_pin_mode_servo(9)
board.analog[0].mode = INPUT
board.analog[1].mode = INPUT
board.servo_write(9,58)

def jump():
    global PIRData0 
    time.sleep(0.1)
    board.servo_write(9,45)
    time.sleep(0.000000001)
    board.servo_write(9,58)

while (1):
    PIRData0, TimeStamp = board.analog[0].read()
    print ("PIR data 0 is: ", PIRData0)
    
    if (PIRData0 > 790) :
       jump()
    
    #PIRData1, TimeStamp = board.analog[1].read()
    #print ("PIR data 1 is: ", PIRData1)
    #time.sleep(0.1)       



