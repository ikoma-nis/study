from sense_hat import SenseHat
class _const:
    class ConstError(TypeError):
        pass
    def _setattr_(self, name, valie):
        if name in self._dict_:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self._dict_[name] = value
        
    #定数宣言
        
    #通信パケット
    REQ_MOVE_MODEL = 0x00 #モデル移動要求
    REQ_PARAMETER_CHANGE = 0x01 #パラメータ変更要求
    RES_MOVE_MODEL = 0x80 #モデル移動応答
    RES_PARAMETER_CHANGE = 0x81 #パラメータ変更応答
        
    DATASIZE_REQ_MOVE_MODEL = 1 #モデル移動要求データサイズ
    DATASIZE_PARAMETER_CHANGE = 2 #パラメータ変更要求データサイズ
    DATASIZE_MOVE_MODEL = 3 #モデル移動応答データサイズ
    DATASIZE_PARAMETER_CHANGE = 1 #パラメータ変更応答データサイズ
    
    PART_COMMAND_ID = 0 #コマンドID
    PART_DATASIZE = 4 #データサイズ部先頭バイト
    
    SIZE_HEADER = 4 #ヘッダ部合計サイズ
    
    #成功失敗判定
    SUCCESS = 1 #成功
    FAILED = 2 #失敗
    
    #ジョイスティック
    NONE = 0 #移動なし
    UP = 1 #上方向
    DOWN = 2 #下方向
    LEFT = 3 #左方向
    RIGHT = 4 #右方向
    
    #LED
    LEDMAX_X = 8; #X軸のLED最大個数
    LEDMAX_Y = 8; #Y軸のLED最大個数
    
    PULGINSERVER =(1) #引数のIndex
    ISMSERVER = (2) #引数のIndex
    
    RED = (128, 0, 0)
    ORANGE = (255, 183, 76)
    YELLOW = (128, 128, 0)
    GREEN = (0, 128, 0)
    LIGHTBLUE = (0, 128, 128)
    BLUE = (0, 0, 128)
    PURPLE = (128, 0, 128)
    WHITE = (128, 128, 128)
    NONE = (0, 0, 0)
    
    LED_PATTERN = (RED, ORANGE, YELLOW, GREEN, LIGHTBLUE, BLUE, PURPLE, WHITE)
    
    #全点灯
    def LED_ALL(self, color):
        
        sense = SenseHat()
        
        sense.clear()
        
        #点灯
        for X in range(self.LEDMAX_X):
            for Y in range(0, self.LEDMAX_Y):
                sense.set_pixel(X, Y, color)
                
    #指定行のみ点灯
    def LED_POSITION(self, color, position):
        
        sense = SenseHat()
        
        sense.clear()
        
        #点灯
        for X in range(self.LEDMAX_X):
            for Y in range(position, self.LEDMAX_Y):
                sense.set_pixel(X, Y, color)
                
    #バツ印を点灯
    def LED_CROSS(self, color):
        
        sense = SenseHat()
        
        sense.clear()
        
        #点灯
        for X in range(0, self.LEDMAX_X):
            for Y in range(self.LEDMAX_Y):
                if(X in (0, 7) and Y in (0, 1, 6, 7)) or (X in (1, 6) and Y in (0, 1, 2, 5, 6, 7)) or (X in (2, 5) and Y in range(1, 7)) or (X in (3, 4) and Y in range(2, 6)):
                    sense.set_pixel(X, Y, color)
                    
    #LED表示種別
    LED_CONNECT = 0
    LED_DISCONNECT = 1
    LED_DISTANCE = 2
    LED_TOUCH_BUILLDING = 3
    LED_CONNECTING = 4
    
import sys
sys.modules[__name__] = _const()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    