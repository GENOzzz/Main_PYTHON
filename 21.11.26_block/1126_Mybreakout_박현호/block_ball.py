import random
from block_table import *
class ball:
    def __init__(self,table,width,height,color,x_speed,y_speed,x_start,y_start):
        self.width=width
        self.height=height
        self.color=color
        self.x_posn=x_start
        self.y_posn=y_start
        self.x_start=x_start
        self.y_start=y_start
        self.x_speed=x_speed
        self.y_speed=y_speed
        
        self.table=table     
        self.ball=self.table.draw_ball(self)
    
    ##함수부    
    def start_position(self):
        self.x_posn=self.x_start
        self.y_posn=self.y_start
        
        
    def start_ball(self, x_speed,y_speed):
        self.x_speed=-x_speed if random.randint(0,1) else x_speed
        self.y_speed=-y_speed if random.randint(0,1) else y_speed
        self.start_position()
        
    def move_next(self):
        self.x_posn+=self.x_speed
        self.y_posn+=self.y_speed
        #공이 왼쪽벽에 부딪쳤을때
        if(self.x_posn<=0):
            self.x_posn=0
            self.x_speed=-self.x_speed
        #공이 오른쪽 벽에 부딪쳤을때
        if(self.x_posn>=(self.table.width-(self.width))):
            self.x_posn=(self.table.width-(self.width))
            self.x_speed=-self.x_speed
        # 공이 위쪽 벽에 부딪쳤을 때
        if(self.y_posn <= 0):
            self.y_posn = 0
            self.y_speed = -self.y_speed
        # 공이 아래쪽 벽에 부딪쳤을 때
        if(self.y_posn >= (self.table.height - (self.height))):
            self.y_posn = (self.table.height - (self.height))
            self.y_speed = -self.y_speed
        # 마지막으로 원의 이동
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.ball, x1, y1, x2, y2)
        
    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0
