from tkinter import *
#import table >>으로 모듈을 불러오면 table 모듈을 이용한 함수는 table.을 붙여주어야함.
from table import *
from ball import *
from bet import *

##전역 변수 초기화
x_speed=10 #공의 x속도
y_speed=0 #공의 y속도
score_left=0 #왼쪽 점수판
score_right=0 #오른쪽 점수판

window=Tk()
window.title("PNG_PONG")

class Line:
    ##생성자
    def __init__(self,table,width,color,x1,y1,x2,y2):
        self.width=width   #선의 두께
        self.x1=x1 #선 시작 x1좌표
        self.y1=y1 #선 시작 y1좌표
        self.x2=x2 #선 끝점 x2좌표
        self.y2=y2 #선 끝점 2y좌표
        self.color=color   #선의색상

        self.tabel=table
        self.line=table.draw_line(self)

##ball_flow()함수부
#def ball_flow():
    #global x_speed,y_speed
    #my_ball.move_next()
    #window.after(10,ball_flow)

##game_flow()함수부
def game_flow():
    global score_left,score_right
    my_ball.move_next()
    #공을 일정 시간마다 움직임
    window.after(20,game_flow)##30밀리초마다 game_flow함수 실행 [5초는 500]
    

    my_bet_L.detect_collision(my_ball)
    my_bet_R.detect_collision(my_ball)

    ##공이 좌우 벽에 충돌했을때 처리
    ##공의 좌표값이 0보다 작을경우 왼쪽 벽에 충돌한 상황
    ##ball 초기화, bet초기화 
    if(my_ball.x_posn<=0):##왼쪽벽에 충돌할경우
        my_ball.stop_ball() ##공을 멈춤 xy_speed를 0으로
        my_ball.start_position() ##공 위치 초기화
        my_bet_L.start_position()
        my_bet_R.start_position()
        #오른쪽 scoreboard 점수 증가
        score_right+=1
        if(score_right>=3):
            score_right="W"
            score_left="L"
        my_table.draw_score(score_left,score_right)

    elif(my_ball.x_posn>=my_table.width):##오른쪽벽에 충돌할경우
        my_ball.stop_ball() ##공을 멈춤 xy_speed를 0으로
        my_ball.start_position() ##공 위치 초기화
        my_bet_L.start_position()
        my_bet_R.start_position()
        #왼쪽 scoreboard 점수 증가
        score_left+=1
        if(score_left>=3):
            score_left="W"
            score_right="L"
        my_table.draw_score(score_left,score_right)
        
    

###restart_game() 함수부
def restart_game(event):
    global score_left,score_right
    #경기 결과가 나왔을 경우 scoreboard도 같이 초기화.
    if(score_left=="W" or score_left=="L"):
        score_left=0
        score_right=0
    my_table.draw_score(score_left,score_right)
    my_bet_L.start_position()
    my_bet_R.start_position()
    my_ball.start_ball(x_speed=x_speed,y_speed=y_speed)

##Table 클래스를 통해 테이블 인스턴스 생성
##(self,window,width,height,bg_color,net_color,out_color)
my_table=Table(window,800,500,"teal","snow","white")

##Line 인스턴스 생성
##(self,table,width,color,x1,y1,x2,y2)
Lline1=Line(my_table,5,"white",7.5,150,107.5,150)
Lline2=Line(my_table,5,"white",7.5,350,107.5,350)
Lline3=Line(my_table,5,"white",107.5,150,107.5,350)
Rline1=Line(my_table,5,"white",790,150,690,150)
Rline2=Line(my_table,5,"white",790,350,690,350)
Rline3=Line(my_table,5,"white",690,150,690,350)

##Ball 인스턴스 생성
##Ball.(self,table,width,height,color,x_speed,y_speed,x_posn,y_posn)
##클래스 호출시 파라미터 명을 적어주면 생성자 입력 순서 관계없이 입력가능.
my_ball=Ball(width=30,height=30,color="gold",x_posn=385,y_posn=235,x_speed=0,y_speed=0,table=my_table)
my_ball.move_next()

##Bet 인스턴스 생성
##Bet.(self,table,width,height,color,x_speed,y_speed,x_posn,y_posn)
my_bet_L=Bet(table=my_table,width=20,height=100,color="dodgerblue",x_speed=20,y_speed=30,x_posn=20,y_posn=200)
my_bet_R=Bet(table=my_table,width=20,height=100,color="tomato",x_speed=20,y_speed=30,x_posn=760,y_posn=200)
L_line=Bet

##함수실행부
game_flow()

window.bind("<space>",restart_game)
##Bet를 제어하기위한 키이벤트 및 연결될 함수 지정
#window.bind("<key>",함수명)
window.bind("w",my_bet_L.move_up)
window.bind("s",my_bet_L.move_down)
window.bind("a",my_bet_L.move_left)
window.bind("d",my_bet_L.move_right)
window.bind("<Up>",my_bet_R.move_up)
window.bind("<Down>",my_bet_R.move_down)
window.bind("<Left>",my_bet_R.move_left)
window.bind("<Right>",my_bet_R.move_right)




window.mainloop()    
