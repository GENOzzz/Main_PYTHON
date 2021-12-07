# 이 파일은 원래 MyPong을 위해 만든 공 클래스입니다.
# 이 클래스는 게임 영역의 측면에 부딪치는 공을 정의합니다.

import table, random

class Ball:
    #### 생성자
    def __init__(self, table, width=14, height=14, colour="red", x_speed=6, y_speed=4, x_start=0, y_start=0):
        self.width = width
        self.height = height
        self.x_posn = x_start
        self.y_posn = y_start
        self.colour = colour

        self.x_start = x_start
        self.y_start = y_start
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.circle = self.table.draw_oval(self)       
    
    #### 메서드    
    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start
        
    def start_ball(self, x_speed, y_speed):
        self.x_speed = -x_speed if random.randint(0,1) else x_speed
        self.y_speed = -y_speed if random.randint(0,1) else y_speed
        self.start_position()
        
    def move_next(self):
        self.x_posn = self.x_posn + self.x_speed
        self.y_posn = self.y_posn + self.y_speed
        # 공이 왼쪽 벽에 부딪쳤을 때:
        if(self.x_posn <= 3):
            self.x_posn = 3
            self.x_speed = -self.x_speed
        # 공이 오른쪽 벽에 부딪쳤을 때:
        if(self.x_posn >= (self.table.width - (self.width - 3))):
            self.x_posn = (self.table.width - (self.width - 3))
            self.x_speed = -self.x_speed
        # 공이 위쪽 벽에 부딪쳤을 때:
        if(self.y_posn <= 3):
            self.y_posn = 3
            self.y_speed = -self.y_speed
        # 공이 아래쪽 벽에 부딪쳤을 때:
        if(self.y_posn >= (self.table.height - (self.height - 3))):
            self.y_posn = (self.table.height - (self.height - 3))
            self.y_speed = -self.y_speed
        # 마지막으로 원의 이동:
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.circle, x1, y1, x2, y2)
        
    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0
