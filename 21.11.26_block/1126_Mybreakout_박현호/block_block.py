from block_table import *
from block_ball import *
class block:
    def __init__(self,table,x_posn,y_posn,color,width=60,height=20):
        self.width=width
        self.height=height
        self.x_posn=x_posn
        self.y_posn=y_posn
        self.color=color
        
        self.table=table
        self.block=self.table.draw_block(self)
        
    ##공과 블럭이 충돌할 경우 
    def detect_collision(self, ball, sides_sweet_spot=True, topnbottom_sweet_spot=False):
        collision_direction = ""
        collision = False
        feel = 5
        # 블럭 변수:
        top = self.y_posn
        bottom = self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_centre = top + (self.height/2)
        h_centre = left + (self.width/2)
        # 공 변수:
        top_b = ball.y_posn
        bottom_b = ball.y_posn + ball.height
        left_b = ball.x_posn
        right_b = ball.x_posn + ball.width
        r = (right_b - left_b)/2
        v_centre_b = top_b + r
        h_centre_b = left_b + r
        
        if((bottom_b > top) and (top_b < bottom) and (right_b > left) and (left_b < right)):
            collision = True
        if(collision):
            if((top_b > top-r) and (bottom_b < bottom+r) and (right_b > right) and (left_b <= right)):
                collision_direction = "E"
                ball.x_speed = abs(ball.x_speed)

            elif((left_b > left-r) and (right_b < right+r) and (bottom_b > bottom) and (top_b <= bottom)):
                collision_direction = "S"
                ball.y_speed = abs(ball.y_speed)
                
            elif((left_b > left-r) and (right_b < right+r) and (top_b < top) and (bottom_b >= top)):
                collision_direction = "N"
                ball.y_speed = -abs(ball.y_speed)

            elif((top_b > top-r) and (bottom_b < bottom+r) and (left_b < left) and (right_b >= left)):
                collision_direction = "W"
                ball.x_speed = -abs(ball.x_speed)

            else:
                collision_direction = "miss"

            if((sides_sweet_spot == True) and (collision_direction == "W" or collision_direction == "E")):
                # 배트의 중심에서 얼마나 먼 거리에서 충돌이 발생했는지 y 값을 찾습니다.
                adjustment = (-(v_centre - v_centre_b))/(self.height/2)
                ball.y_speed = feel * adjustment
                print("YYYY")

            if((topnbottom_sweet_spot == True) and (collision_direction == "N" or collision_direction == "S")):
                # 배트의 중심에서 얼마나 먼 거리에서 충돌이 발생했는지 x 값을 찾습니다.
                adjustment = (-(h_centre - h_centre_b))/(self.width/2)
                ball.x_speed = feel * adjustment
                print("XXXX")

            return (collision, collision_direction)