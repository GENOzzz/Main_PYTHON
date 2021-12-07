#Sunny Pingpong - main
from tkinter import *
import random
#import table, ball

# 전역 변수 초기화
x_speed = 10 # x속도
y_speed = 0 # y속도
score_left = 0 # 왼쪽 득점판
score_right = 0  # 오른쪽 득점판
first_serve = True # 첫번째 서브 여부

# 클래스 및 함수부

# Table 클래스
# Table의 처리 공간을 2D 직사각형으로 정의

class Table:
    ### 생성자
    def __init__(self, window, width, height, bg_color, net_color, net):
        
        self.width=width
        self.height=height
        self.bg_color=bg_color
        self.net_color=net_color
        self.net=net

        # tkinter 모듈의 Canvas 클래스를 통해 캔버스 생성:
        self.canvas=Canvas(window, width=self.width, height=self.height, bg=self.bg_color)
        self.canvas.pack() # 캔버스 출력

        # tkinter 모듈의 create_line() 메서드를 사용하여 캔버스에 네트 추가:
        # create_line(startX, startY, endX, endY, width=네트두께, fill=네트컬러, dash=(길이, 간격))
        if(net=="vertical"):
            self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width=2, fill=net_color, dash=(15, 23))
        else:
            self.canvas.create_line(0, self.height/2, self.width, self.height/2, width=2, fill=net_color, dash=(15, 23))

        # 득점판 추가:
        font = ("monaco", 72)
        self.scoreboard = self.canvas.create_text(300, 65, font=font, fill = "darkgreen")
        
    #### 함수부

    # Canvas에 타원을 추가하는 함수:
    def draw_oval(self, oval):
        x1 = oval.x_posn
        x2 = oval.x_posn + oval.width
        y1 = oval.y_posn
        y2 = oval.y_posn + oval.height
        c = oval.color
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)
        #canvas.create_oval(288, 188, 312, 212, fill="red")


    # Canvas에 직사각형을 추가하는 함수:
    def draw_rectangle(self, rectangle):
        x1 = rectangle.x_posn
        x2 = rectangle.x_posn + rectangle.width
        y1 = rectangle.y_posn
        y2 = rectangle.y_posn + rectangle.height
        c = rectangle.color
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)
        #create_rectangle(20, 150, 35, 250, fill="blue")

    # canvas의 아이템을 조작할 수 있는 도구:
    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)

    # canvas에 득점판을 추가하는 도구:
    def draw_score(self, left, right):
        scores = str(right) + "  " + str(left)
        self.canvas.itemconfigure(self.scoreboard, text=scores)        

class Ball:
    #### 생성자
    def __init__(self, table, width, height, color, x_speed, y_speed, x_posn, y_posn):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.color = color

        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.circle = self.table.draw_oval(self)

    #### 함수부    
    def move_next(self):
        self.x_posn = self.x_posn + self.x_speed # 현재 공의 위치에 이동할 거리 x 를 추가
        self.y_posn = self.y_posn + self.y_speed # 현재 공의 위치에 이동할 거리 x 를 추가

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

    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start
        
    def start_ball(self, x_speed, y_speed):
        self.x_speed = -x_speed if random.randint(0,1) else x_speed
        self.y_speed = -y_speed if random.randint(0,1) else y_speed
        self.start_position()    

    def stop_ball(self):
        self.x_speed = 0
        self.y_speed = 0        

class Bat:
    #### 생성자
    def __init__(self, table, width, height, x_posn, y_posn, color, x_speed = 23, y_speed = 23):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.color = color

        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.rectangle = self.table.draw_rectangle(self)

    def detect_collision(self, ball, sides_sweet_spot=True, topnbottom_sweet_spot=False):
        collision_direction = ""  # 충돌 방향 저장
        collision = False           # 충돌이 감지되면 True 로 바뀜
        feel = 5                         # 배트에서 공을 튕겨낸 다음 반사 각도와 반응 정도를 조정
        # 배트 변수:
        top = self.y_posn
        bottom = self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_center = top + (self.height/2)
        h_center = left + (self.width/2)
        # 공 변수:
        top_b = ball.y_posn
        bottom_b = ball.y_posn + ball.height
        left_b = ball.x_posn
        right_b = ball.x_posn + ball.width
        r = (right_b - left_b)/2
        v_center_b = top_b + r
        h_center_b = left_b + r
        
        if((bottom_b > top) and (top_b < bottom) and (right_b > left) and (left_b < right)):
            collision = True
            print("충돌")
            
        # 만약 충돌했다면 어느 방향으로 충돌했는지 collision_direction에 저장        
        if(collision):
            if((top_b > top-r) and (bottom_b < bottom+r) and (right_b > right) and (left_b <= right)):
                collision_direction = "E"
               # abs() 함수는 숫자의 부호를 제거하는 함수, 속도 값을 얻는데 사용
                # abs() 함수는 공이 배트의 어느 부분에 충돌했는지에 따라 공이 튀는 방향 바꿈
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
                adjustment = (-(v_center - v_center_b))/(self.height/2)
                ball.y_speed = feel * adjustment

            if((topnbottom_sweet_spot == True) and (collision_direction == "N" or collision_direction == "S")):
                # 배트의 중심에서 얼마나 먼 거리에서 충돌이 발생했는지 x 값을 찾습니다.
                adjustment = (-(h_centre - h_centre_b))/(self.width/2)
                ball.x_speed = feel * adjustment

            return (collision, collision_direction)                
            
    def move_up(self, master):
        self.y_posn = self.y_posn - self.y_speed
        if(self.y_posn <= 0):
           self.y_posn = 0
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)
        
    def move_down(self, master):
        self.y_posn = self.y_posn + self.y_speed
        far_bottom = self.table.height - self.height
        if(self.y_posn >= far_bottom):
            self.y_posn = far_bottom
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start        



#### 함수:
def game_flow():

    global first_serve
    global score_left
    global score_right
    
    # 첫번째 서브를 기다립니다:
    if(first_serve == True):
        my_ball.stop_ball()
        first_serve = False
    
    # 공이 배트에 닿았는지 충돌 확인:
    bat_L.detect_collision(my_ball)
    bat_R.detect_collision(my_ball)

    # 왼쪽 벽에서 공이 부딪히는지 감지:
    if(my_ball.x_posn <= 3):
        my_ball.stop_ball()   # 공을 멈춤, y_speed를 0으로 설정
        my_ball.start_position() # 공의 위치 초기화
        bat_L.start_position() # bat_L 배트 위치 초기화
        bat_R.start_position() # bat_R 배트 위치 초기화
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250) # bat_L 배트 초기값을 이동
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250) # bat_R 배트 초기값을 이동
        score_left = score_left + 1 # 왼쪽 득점 1 추가
        if(score_left >= 5):  # 왼쪽 득점 10 이상일 경우 왼쪽 글자 W(Win) 표시
            score_left = "W"
            score_right = "L"
        first_serve = True
        my_table.draw_score(score_left, score_right)

    # 오른쪽 벽에서 공이 부딪치는지 감지:
    if(my_ball.x_posn + my_ball.width >= my_table.width - 3):
        my_ball.stop_ball()
        my_ball.start_position()
        bat_L.start_position()
        bat_R.start_position()
        my_table.move_item(bat_L.rectangle, 20, 150, 35, 250)
        my_table.move_item(bat_R.rectangle, 575, 150, 590, 250)
        score_right = score_right + 1
        if(score_right >= 5):
            score_right = "W"
            score_left = "L"
        first_serve=True
        my_table.draw_score(score_left, score_right)
     
    my_ball.move_next() 
    window.after(30, game_flow) # 30밀리초마다 game_flow 함수 실행 , ex 5초는 500

# restart_game 함수:
def restart_game(master):
    global score_left
    global score_right
    my_ball.start_ball(x_speed=x_speed, y_speed=y_speed)
    if(score_left == "W" or score_left == "L"):
        score_left = 0
        score_right = 0
    my_table.draw_score(score_left, score_right)    

# 메인부
window=Tk()
window.title("MyPingPong")

### 테이블 생성
# table 모듈의 Table 클래스로부터 볼 주문 생성
'''
# 1. 클래스 없이 테이블 생성  , 테이블 가로 , 네트선 세로
canvas=Canvas(window, width=600, height=400, bg="black")
canvas.pack()
canvas.create_line(300, 0, 300, 400, width=2, fill="green", dash=(15, 23))
'''

# 2. 클래스를 활용한  테이블 생성
# 2-1 문서내 클래스를 사용할 경우 클래스명만 입력
my_table = Table(window, 600,400,"black","green","vertical") # 테이블 가로 , 네트선 세로 
#my_table = Table(window, 400,600,"black","green","etc") # 테이블 세로, 네트선 가로

'''
# 2-2모듈의 클래스를 사용할 경우 모듈명.클래스명 으로 입력
my_table = table.Table(window, 600,400,"black","green","vertical") # 가로

canvas.create_line(300, 0, 300, 400, width=2, fill="green", dash=(15, 23))
canvas.create_text(300, 65, font=("monaco", 72), fill = "darkgreen")

### 공  생성
canvas.create_oval(288, 188, 312, 212, fill="red")

### 배트  생성
canvas.create_rectangle(20, 150, 35, 250, fill="blue")
canvas.create_rectangle(575, 150, 590, 250, fill="yellow")
'''

### 볼 생성
# ball 모듈의 Ball 클래스로부터 볼 주문 생성
my_ball = Ball(table=my_table, x_speed=0, y_speed=0, width=24, height=24, color="red", x_posn=288, y_posn=188)

### 배트 생성
# Bat 클래스로부터 배트를 주문
bat_L = Bat(table=my_table, width=15, height=100, x_posn=20, y_posn=150, color="blue")
bat_R = Bat(table=my_table, width=15, height=100, x_posn=575, y_posn=150, color="yellow")

# 배트를 제어하기 위해 키보드의 키에 연결
window.bind("a", bat_L.move_up)
window.bind("z", bat_L.move_down)
window.bind("<Up>", bat_R.move_up)
window.bind("<Down>", bat_R.move_down)

# game_flow 반복문 호출
game_flow()

# 스페이스바를 눌러 게임 시작 또는 재시작
window.bind("<space>", restart_game)

window.mainloop()
