# MyPong의 주된 파일을 만듭니다.

from tkinter import *
import table, ball, bat, random


window = Tk()
window.title("MyBreakout")
my_table = table.Table(window)

# 전역 변수 초기화
x_velocity = 4
y_velocity = 10
first_serve = True

# Ball 공장으로부터 볼을 주문합니다
my_ball = ball.Ball(table = my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, colour="red", x_start=288, y_start=188)

# Bat 공장으로부터 배트를 주문합니다
bat_B = bat.Bat(table = my_table, width=100, height=10,
                x_posn=250, y_posn=370, colour="blue")

# Bat 클래스로부터 배트를 주문하지만 이것은 벽돌을 호출하는 것은 아닙니다.
bricks = []
b=1
while b < 7:
    i=80
    bricks.append(bat.Bat(table = my_table, width=50, height=20,
                          x_posn=(b*i), y_posn=75, colour="green"))
    b = b+1

        
#### 함수:
def game_flow():
    global first_serve
    # 첫번째 서브를 기다립니다:
    if(first_serve==True):
        my_ball.stop_ball()
        first_serve = False
    
    # 배트에 공이 충돌하는지 감지
    bat_B.detect_collision(my_ball, sides_sweet_spot=False, topnbottom_sweet_spot=True)
    

    # 벽돌에 공이 충돌하는지 감지
    for b in bricks:
        #  b번째 공이 벽돌에 충돌했다면 벽돌을 화면에서 지우고, 배열에서 삭제
        if(b.detect_collision(my_ball, sides_sweet_spot=False) != None):
            print(b.detect_collision(my_ball, sides_sweet_spot=False))
            my_table.remove_item(b.rectangle)
            bricks.remove(b)
        # 벽돌이 없다면 점수 출력
        if(len(bricks) == 0):
            my_ball.stop_ball()
            my_ball.start_position()
            my_table.draw_score("", "  YOU WIN!")              
            
    # 아래쪽 벽에 공이 충돌하는지 감지
    if(my_ball.y_posn >= my_table.height - my_ball.height):
        my_ball.stop_ball()
        my_ball.start_position()
        first_serve = True
        my_table.draw_score("", "  WHOOPS!")
        
    my_ball.move_next()
    window.after(50, game_flow)
    
def restart_game(master):
    my_ball.start_ball(x_speed=x_velocity, y_speed=y_velocity)
    my_table.draw_score("", "")

# 배트를 제어할 수 있도록 키보드의 키와 연결
window.bind("<Left>", bat_B.move_left) #키보드 왼쪽키를 누르면 bat_B를 통해 move_left함수 호출
window.bind("<Right>", bat_B.move_right) #키보드 오른쪽키를 누르면 bat_B를 통해 move_Right함수 호출

# 스페이스 키를 게임 재시작 기능과 연결
window.bind("<space>", restart_game)

game_flow()
window.mainloop()
