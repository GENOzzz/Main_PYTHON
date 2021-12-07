from tkinter import *
##randint 함수를 불러오기 위한 모듈 임포트 
import random

##전역 변수 초기화
x_speed=25 #공의 x속도
y_speed=10 #공의 y속도

window=Tk()
window.title("PNG_PONG")

###Table 클래스 생성
class Table:
    
    ##생성자
    def __init__(self,window,width,height,bg_color,net_color,out_color):
        self.width=width
        self.height=height
        self.bg_color=bg_color
        self.net_color=net_color
        self.out_color=out_color

#Talbe 클래스 내에서 캔버스생성
        self.canvas=Canvas(window,width=self.width,height=self.height,bg=self.bg_color)
        self.canvas.pack()

        self.canvas.create_line((self.width/2),7.5,self.width/2,self.height-2.5,width=2,fill=net_color,dash=(20,30))
        self.canvas.create_line(7.5,7.5,self.width-7.5,7.5,width=5,fill=out_color)
        self.canvas.create_line(10,10,10,self.height-2.5,width=5,fill=out_color)
        self.canvas.create_line(self.width-10,self.height-2.5,self.width-10,10,width=5,fill=out_color)
        self.canvas.create_line(self.width-10,self.height-5,10,self.height-5,width=5,fill=out_color)
        self.canvas.create_arc(40,40,-15,-20,extent=-90,outline="white",style=ARC,width=3)
        self.canvas.create_arc(-20,524,40,462,extent=90,outline="white",style=ARC,width=3)
        self.canvas.create_arc(820,524,760,462,start=90,extent=90,outline="white",style=ARC,width=3)
        self.canvas.create_arc(760,40,815,-20,start=180,extent=90,outline="white",style=ARC,width=3)
        
        


    ##함수정의
    ##Canvas(Table)에 선을 추가하는 함수
    def draw_line(self,line):
        x1=line.x1
        y1=line.y1
        x2=line.x2
        y2=line.y2
        color=line.color
        return self.canvas.create_line(x1,y1,x2,y2,fill=color)

    #Canvas(Table)에 타원을 추가하는 함수
    def draw_circle(self,circle):
        x1=circle.x1
        y1=circle.y1
        x2=circle.x2
        y2=circle.y2
        outline=circle.outline
        whidth=circle.width
        return self.canvas.create_oval(x1,y1,x2,y2,outline=outline,width=width)
        
    ##Canvas(Table)에 원(Ball)을 추가하는 함수.
    def draw_oval(self,oval):
        x1=oval.x_posn
        x2=oval.x_posn+oval.width
        y2=oval.y_posn
        y1=oval.y_posn+oval.height
        color=oval.color
        return self.canvas.create_oval(x1,y1,x2,y2,fill=color)

    ##Canvas(Table)에 사각형(bet)을 추가하는 함수
    def draw_rect(self,rect):
        x1=rect.x_posn
        x2=rect.x_posn+rect.width
        y2=rect.y_posn
        y1=rect.y_posn+rect.height
        color=rect.color
        return self.canvas.create_rectangle(x1,y1,x2,y2,fill=color)

    ##Canvas(Tabel)에 아이템(ball과 bet)을 조작할 수 있는 함수 coords() 이용
    ##coords()는 입력받은 값으로 속성값 업데이트 하는 함수
    #변경된 위치 값으로 item의 위치 변경
    def move_item(self,item,x1,y1,x2,y2):
        self.canvas.coords(item,x1,y1,x2,y2)


class Circle:
    def __init__(self,table,width,outline,x1,y1,x2,y2):
        self.width=width
        self.outline=outline
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

        self.table=table
        self.circle=self.table.draw_circle(self)

class Line:
    ##생성자
    def __init__(self,table,width,color,x1,y1,x2,y2):
        self.width=width   #선의 두께
        self.x1=x1 #선 시작 x1좌표
        self.y1=y1 #선 시작 y1좌표
        self.x2=x2 #선 끝점 x2좌표
        self.y2=y2 #선 끝점 2y좌표
        self.color=color   #선의색상

        self.table=table
        self.line=table.draw_line(self)
        
        

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
        self.x_speed=0
        self.y_speed=0
        


##Bet 클래스 생성
class Bet:
    ##생성자                                   ##x이동은 아직은 의미없음(위아래로만 움직이게)
    def __init__(self,table,width,height,color,x_speed,y_speed,x_posn,y_posn):
        self.width=width   #베트의 가로사이즈
        self.height=height #베의 세로사이즈
        self.x_posn=x_posn #베트의 x좌표
        self.y_posn=y_posn #베트의y좌표
        self.color=color   #베트의 색상

        self.x_start=x_posn #베트의 초기위치 x,y start에 저장.
        self.y_start=y_posn
        self.x_speed=x_speed #베트가 움직이게 보이게 하기위한 speed x,y
        self.y_speed=y_speed

        self.table=table
        self.rect=self.table.draw_rect(self)

    ##함수부
    ##베트를 위로 움직이는 함수
    def move_up(self,master):
        self.y_posn-=self.y_speed ##y_speed의 값 만큼 y_posn값을 뺌
        if(self.y_posn <=0): ##베트가 화면 상단에 걸릴때
            self.y_posn=0
        x1=self.x_posn
        x2=self.x_posn+self.width
        y2=self.y_posn      ##변경된 y_posn의 값을 y1에 반
        y1=self.y_posn+self.height

        ##변경된 값으로 아이템을 옮김
        ##Table클래서의 move_item()함수 실행
        self.table.move_item(self.rect,x1,y1,x2,y2)

    def move_down(self,master):
        self.y_posn+=self.y_speed ##y_speed의 값 만큼 y_posn값을 뺌
        if(self.y_posn >=400): ##bet가 화면 하단에 걸릴때
            self.y_posn=400
        x1=self.x_posn
        x2=self.x_posn+self.width
        y2=self.y_posn      ##변경된 y_posn의 값을 y1에 반
        y1=self.y_posn+self.height

        self.table.move_item(self.rect,x1,y1,x2,y2)

    ##ball과 bet의 충돌 감지및 처리함수
    def detect_collision(self,ball):
        collision_direction="" #충돌방향저장
        collision=False        #충돌이 감지되면 True로 바뀜
        feel=5                 #배트에서 공을 튕겨낸 다음반사 각도와 반응 정도를 조
        
        ##배트변수
        top=self.y_posn
        bottom=self.y_posn+self.height
        left=self.x_posn
        right=self.x_posn+self.width
        v_center=top+(self.height/2)
        h_center=left+(self.width/2)

        ##공변수
        top_b=ball.y_posn
        bottom_b=ball.y_posn+ball.height
        left_b=ball.x_posn
        right_b=ball.x_posn+ball.width
        r=(right_b-left_b)/2 ##반지름
        v_center_b=top_b+r
        h_center_b=left_b+r

        ##ball과 bet의 충돌감지
        #공의 바닥이 배트의 탑보다 크고 공의 탑이 배트의 바닥보다 작고
        #공의 오른쪽이 배트의 왼쪽보다 크고 공의 왼쪽이 배트의 오른쪽보다 작을때 충돌.
        if((bottom_b>top)and(top_b<bottom)and(right_b>left)and(left_b<right)):
            collision=True #collision값 변경
            print("충돌")

        if(collision):##만약 collision이 True면
            #공의 오른쪽 부분이 배트의 오른쪽부분보다 크고 ... 배트의 오른쪽에서 공이 충돌
            if((right_b>right)and(left_b<=right)and(top_b>top-r)and(bottom_b<bottom+r)):
                collision_direction="E"
                ##abs는 숫자의 부호를 제거하는 함수 속도,값을 얻는데 사용
                ##공이 배트의 어느 부분에 충돌했는지에 따라 공이 튀는 방향 바꿈.
                ball.x_speed=abs(ball.x_speed) ##공이 x의 양수값으로 (오른쪽으로 이동)
                ##공의 중심이 배트의 중심에서 얼마나 먼 거리에서 충돌이 발생했는지 계산하여 y좌표값에 적용
                adjustment=(-(v_center-v_center_b))/(self.height/2)
                print(adjustment)
                ##멀리서 충돌할 수록 y는 더욱 크게 꺾임
                ball.y_speed=feel*adjustment

            
            elif((left_b<left)and(right_b>=left)and(top_b>top-r)and(bottom_b<bottom+r)):
                collision_direction="W"
                ball.x_speed=-abs(ball.x_speed)

                adjustment=(-(v_center-v_center_b))/(self.height/2)
                print(adjustment)
                ball.y_speed=feel*adjustment
    
            return(collision,collision_direction)

    ##Bet의 초기 위치값 지정
    def start_position(self):
        self.x_posn=self.x_start
        self.y_posn=self.y_start
        x1=self.x_posn
        y1=self.y_posn
        x2=self.x_posn+self.width
        y2=self.y_posn+self.height
        self.table.move_item(self.rect,x1,y1,x2,y2)


 
##game_flow()함수부
def game_flow():
    my_ball.move_next()
    #공을 일정 시간마다 움직임
    window.after(30,game_flow)##30밀리초마다 game_flow함수 실행 [5초는 500]

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

    elif(my_ball.x_posn>=my_table.width):##오른쪽벽에 충돌할경우
        my_ball.stop_ball() ##공을 멈춤 xy_speed를 0으로
        my_ball.start_position() ##공 위치 초기화
        my_bet_L.start_position()
        my_bet_R.start_position()
    

###restart_game() 함수부
def restart_game(event):
    my_ball.start_ball(x_speed=x_speed,y_speed=y_speed)

##Table 클래스를 통해 테이블 인스턴스 생성
##(self,window,width,height,bg_color,net_color,out_color)
my_table=Table(window,800,500,"teal","snow","white")

#Circle인스턴스 생성
#(self,table,width,outline,x1,y1,x2,y2)
CenterCircle=Circle(my_table,"white",3,350,200,450,300)

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
my_bet_L=Bet(table=my_table,width=20,height=100,color="dodgerblue",x_speed=0,y_speed=30,x_posn=20,y_posn=200)
my_bet_R=Bet(table=my_table,width=20,height=100,color="tomato",x_speed=0,y_speed=30,x_posn=760,y_posn=200)
L_line=Bet

##함수실행부
game_flow()

window.bind("<space>",restart_game)
##Bet를 제어하기위한 키이벤트 및 연결될 함수 지정
#window.bind("<key>",함수명)
window.bind("w",my_bet_L.move_up)
window.bind("s",my_bet_L.move_down)
window.bind("<Up>",my_bet_R.move_up)
window.bind("<Down>",my_bet_R.move_down)




window.mainloop()    
