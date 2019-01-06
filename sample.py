import const
import sys
import socket
import traceback
from sense_hat import SenseHat
from time import sleep

#LED点灯関数
def turnOnLED(displayType):
    global distance
    global previousLED
    global distanceVal
    
    #接続中
    if displayType == const.LED_CONNECTING:
        
        #点灯
        const.LED_ALL(const.WHITE)
        
    #接続    
    elif displayType ==const.LED_CONNECT and previousLED[0] != const.LED_CONNECT:
        
        #点灯
        const.LED_ALL(const.YELLOW)
        
        sleep(1)
        
    #接続断
    elif displayType == const.LED_DISCONNECT and previousLED[0] != const.LED_DISCONNECT:
        
        #点灯
        const.LED_ALL(const.RED)