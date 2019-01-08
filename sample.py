

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
        
        #点灯状態を１秒維持
        sleep(1)
        
    #接続断
    elif displayType == const.LED_DISCONNECT and previousLED[0] != const.LED_DISCONNECT:
        
        #点灯
        const.LED_ALL(const.RED)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    return True


#送信関数
def sendRequest(command):
    
    global direction
    global Connected
    
    #モデル移動要求
    if command == const.REQ_MOVE_MODEL:
        sendBuf = const.REQ_MOVE_MODEL.to_bytes(1, 'little') + const.DATASIZE_REQ_MOVE_MODEL.to_bytes(3, 'little') + direction.to_bytes(1, 'little')
        
        #パケット格納後のデータ値を初期化
        derection = 0
    
    #パラメータ変更要求
    elif command == const.REQ_PARAMETER_CHANGE:
        sendBuf = const.REQ_PARAMETER_CHANGE.to_bytes(1, 'little') + const.DATASIZE_REQ_PARAMETER_CHANGE.to_bytes(3, 'little') + const.MODELSPEED.to_bytes(2, 'little')
        
    else:
        pass
    try:
        #パケット送信
        client.send(sendBuf)
        
    except KeyboardInterrupt:
        sys.exit()
        
    except OSError:
        #接続エラーLED表示
        turnOnLED(const.LED_DISCONNECT)
        Connected = False
        client.close()
        
    except:
        print(traceback.print_exc(), "送信処理エラー")
        
        #接続エラーLED表示
        turnOnLED(const.LED_DISCONNECT)
        
        client.close()
        sys.exit()
        
    return True

#データ受信時の成功失敗チェック
def successCheck(response):
    
    if response == const.SUCCESS:
        return True
    else:
        return False

#データ受信時のデータサイズチェック
def dataSizeCheck(response):
    
    #データサイズ値を生成
    size = response[1] + (response[2] * 16) + (response[3] * 256)
    
    #データサイズチェック
    if response[const.PART_COMMAND_ID] == const.RES_MOVE_MODEL:
        if size == const.DATASIZE_RES_MOVE_MODEL:
            pass
        else:
            return False
        
    elif response[const.PART_COMMAND_ID] ==const.RES_PARAMETER_CHANGE:
        if size == const.DATASIZE_RES_PARAMETER_CHANGE:
            pass
        else:
            return False
        
    else:
        return False
    
    return True

#モデル移動応答受信処理
def recvMovemodel(response):
    
    global distance
    
        