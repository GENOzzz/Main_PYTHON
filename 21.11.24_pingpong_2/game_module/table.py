from tkinter import *
#table module
###Table 클래스 생성
score_left=0
score_right=0
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

        #Table클래스 내에서 테두리 선 생성
        self.canvas.create_line((self.width/2),7.5,self.width/2,self.height-2.5,width=2,fill=net_color,dash=(20,30))
        self.canvas.create_line(7.5,7.5,self.width-7.5,7.5,width=5,fill=out_color)
        self.canvas.create_line(10,10,10,self.height-2.5,width=5,fill=out_color)
        self.canvas.create_line(self.width-10,self.height-2.5,self.width-10,10,width=5,fill=out_color)
        self.canvas.create_line(self.width-10,self.height-5,10,self.height-5,width=5,fill=out_color)
        #Table클래스 내에서 모서리 호 생성
        self.canvas.create_arc(40,40,-15,-20,extent=-90,outline="white",style=ARC,width=3)
        self.canvas.create_arc(-20,524,40,462,extent=90,outline="white",style=ARC,width=3)
        self.canvas.create_arc(820,524,760,462,start=90,extent=90,outline="white",style=ARC,width=3)
        self.canvas.create_arc(760,40,815,-20,start=180,extent=90,outline="white",style=ARC,width=3)
        self.canvas.create_oval(350,200,450,300,outline="white",width=3)

        #Table 클래스 내에서 득점판 생성
        font=("monaco",60)
        self.scoreboard=self.canvas.create_text(self.width/2,90,font=font,fill="snow",text=str(score_left)+" "+str(score_right))


    ##함수정의
    ##Canvas(Table)에 선을 추가하는 함수
    def draw_line(self,line):
        x1=line.x1
        y1=line.y1
        x2=line.x2
        y2=line.y2
        color=line.color
        return self.canvas.create_line(x1,y1,x2,y2,fill=color)
        
    ##Canvas(Table)에 타원(Ball)을 추가하는 함수.
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

    ##Canvas(Table)에 아이템(ball과 bet)을 조작할 수 있는 함수 coords() 이용
    ##coords()는 입력받은 값으로 속성값 업데이트 하는 함수
    #변경된 위치 값으로 item의 위치 변경
    def move_item(self,item,x1,y1,x2,y2):
        self.canvas.coords(item,x1,y1,x2,y2)

    #Canvas(Table)에 득점판을 갱신하는 함수
    def draw_score(self,left,right):
        global score_left,score_right
        score=str(left)+" "+str(right)
        self.canvas.itemconfigure(self.scoreboard,text=score)
