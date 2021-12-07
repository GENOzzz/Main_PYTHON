import random,table #랜덤모듈
#ball module
##Ball 클래스 생성
class Ball:
    ##생성자                               ##1pix움직이면 천천히10px움직이면 빨리가는것처럼보임
    def __init__(self,table,width,height,color,x_speed,y_speed,x_posn,y_posn):
        self.width=width   #공의 가로사이즈
        self.height=height #공의 세로사이즈
        self.x_posn=x_posn #공의 x좌표
        self.y_posn=y_posn #공의y좌표
        self.color=color   #공의 색상

        self.x_start=x_posn #공의 초기위치 x,y
        self.y_start=y_posn
        self.x_speed=x_speed #공이 움직이게 보이게 하기위한 speed x,y
        self.y_speed=y_speed

        self.table=table #공을 테이블에 띄우기위해 테이블 입력
        self.circle=self.table.draw_oval(self) #입력받은 테이블위에 ball을 draw_oval(함수)
                                               #테이블 위에 공을 그려야 하므로 테이블클래스에서 정의

    ##함수부
    #Ball이 움직이는 부분
    def move_next(self):
        self.x_posn+= self.x_speed #현재 공의 위치에 이동할거리 x를 추가
        self.y_posn+= self.y_speed #현재 공의 위치에 이동할거리 y를 추가

        #공이 위쪽 벽에 충돌했을때
        if(self.y_posn<=0):
            self.y_posn=0
            self.y_speed=-self.y_speed
        if(self.y_posn>=(self.table.height-self.height)):
           self.y_posn=(self.table.height-self.height)
           self.y_speed=-self.y_speed
        
        x1=self.x_posn
        x2=self.x_posn+self.width
        y1=self.y_posn
        y2=self.y_posn+self.height
        self.table.move_item(self.circle,x1,y1,x2,y2)

    ##공의 초기 위치값 지정
    def start_position(self):
        self.x_posn=self.x_start
        self.y_posn=self.y_start

    ##전역변수x_speed의 값을 불러와 공의 속도에 대입,랜덤하게 생성된 값에의해 +또는 -스피드 값이적용
    def start_ball(self,x_speed,y_speed):
        self.x_speed=-x_speed if random.randint(0,1)else x_speed
        self.y_speed=-y_speed if random.randint(0,1)else y_speed
        self.start_position()

    def stop_ball(self):
        self.width=30
        self.height=30
        self.x_speed=0
        self.y_speed=0
