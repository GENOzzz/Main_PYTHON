from tkinter import *
from block_table import *
from block_ball import *
from block_bat import *
from block_block import *



window=Tk()
window.title("BLOCK_BREAK")
my_table=table(window,600,800,"grey23") 
##전역 변수 초기화
x_velocity=4
y_velocity=10
first_serve=True
text=["U","Ua","Uar","Uare","UareS","UareSo","UareSoC","UareSoCo","UareSoCoo","UareSoCool"]

my_bat=bat(table=my_table,width=120,height=20,color="aquamarine",x_start=240,y_start=700,x_speed=40)
my_ball=ball(table=my_table,width=16,height=16,color="snow",x_speed=100,y_speed=100,x_start=300-8,y_start=500-8)

bricks = []
def cb():
    yy=60
    for i in range(6):
        xx=22
        for k in range(6):
            if (i==0 and k==0)or(i==0 and k==5):
                bricks.append(block(table=my_table,x_posn=xx,y_posn=yy,color="black"))
                xx+=100
                continue
            elif i<3:
                if (i==2 and k==3) or (i==2 and k==4):
                    bricks.append(block(table=my_table,x_posn=xx,y_posn=yy,color="dodgerblue"))
                    xx+=100
                    continue
                bricks.append(block(table=my_table,x_posn=xx,y_posn=yy,color="tomato"))
                xx+=100
            else:
                if(i==3 and k==1) or (i==3 and k==2):
                    bricks.append(block(table=my_table,x_posn=xx,y_posn=yy,color="tomato"))
                    xx+=100
                    continue
                elif(i==5 and k==0) or (i==5 and k==5):
                    bricks.append(block(table=my_table,x_posn=xx,y_posn=yy,color="black"))
                    xx+=100
                    continue
                bricks.append(block(table=my_table,x_posn=xx,y_posn=yy,color="dodgerblue"))
                xx+=100
            
        yy+=40
#함수정의

def restart_game(master):
    my_ball.start_ball(x_speed=x_velocity,y_speed=y_velocity)
    my_table.draw_score("", "")
    my_table.draw_text(" ")
    my_bat.start_position()
    if(len(bricks)==0):
        cb()

def game_flow():
    global first_serve
    # 첫번째 서브를 기다립니다:
    if(first_serve==True):
        my_ball.stop_ball()
        first_serve = False
    
    # 배트에 공이 충돌하는지 감지
    if(my_bat.detect_collision(my_ball, sides_sweet_spot=False, topnbottom_sweet_spot=True)):
                                            ##충돌이 발생할시 RGB값을 랜덤으로 받아 해당 객체의 색을 랜덤으로 바꾸는 코드.
        my_table.change_color(my_ball.ball,"#{:02x}{:02x}{:02x}".format(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        my_table.change_color(my_bat.bat,"#{:02x}{:02x}{:02x}".format(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
 
    # 벽돌에 공이 충돌하는지 감지
    for i in bricks:
        #  공이 i번째 벽돌에 충돌했다면 벽돌을 화면에서 지우고, 배열에서 삭제
        if(i.detect_collision(my_ball, sides_sweet_spot=False) != None):
            print(i.detect_collision(my_ball, sides_sweet_spot=False))
            my_table.change_color(my_ball.ball,"#{:02x}{:02x}{:02x}".format(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            my_table.remove_item(i.block)
            bricks.remove(i)
            
        if(len(bricks)<10):
            for i in range(10-len(bricks)):
                my_table.draw_text(str(text[i]))
                
        # 벽돌이 없다면 점수 출력
        if(len(bricks) == 0):
            my_ball.stop_ball()
            my_ball.start_position()
            my_bat.start_position()
            my_table.draw_score("", "   YOU WIN!")                      
            
    # 아래쪽 벽에 공이 충돌하는지 감지
    if(my_ball.y_posn >= my_table.height - my_ball.height):
        my_ball.stop_ball()
        my_ball.start_position()
        my_bat.start_position()
        first_serve = True
        my_table.draw_score("", "   LOSER :-p ")

    my_ball.move_next()
    window.after(20, game_flow)
    
    
#window.bind("<f>",stop_game)##boolean으로 게임을 멈췄다 진행시켰다
window.bind("<space>",restart_game)##게임 재시작
cb()
game_flow()
window.bind("<Left>",my_bat.move_left)##배트 왼쪽이동
window.bind("<Right>",my_bat.move_right)##배트 오른쪽 이동

window.mainloop()
