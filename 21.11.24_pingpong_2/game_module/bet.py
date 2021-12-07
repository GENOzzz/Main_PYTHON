import table,ball
#bet module    
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
        y1=self.y_posn+self.height
        x2=self.x_posn+self.width
        y2=self.y_posn      ##변경된 y_posn의 값을 y1에 반
        

        ##변경된 값으로 아이템을 옮김
        ##Table클래서의 move_item()함수 실행
        self.table.move_item(self.rect,x1,y1,x2,y2)

    def move_down(self,master):
        self.y_posn+=self.y_speed ##y_speed의 값 만큼 y_posn값을 뺌
        if(self.y_posn >=self.table.height-self.height): ##bet가 화면 하단에 걸릴때
            self.y_posn=self.table.height-self.height
        x1=self.x_posn
        y1=self.y_posn+self.height ##변경된 y_posn의 값을 y1에 반
        x2=self.x_posn+self.width
        y2=self.y_posn      
        

        self.table.move_item(self.rect,x1,y1,x2,y2)

    def move_left(self,master):
        self.x_posn-=self.x_speed ##y_speed의 값 만큼 y_posn값을 뺌
        if(self.x_posn <=0): ##bet가 화면 하단에 걸릴때
            self.x_posn=0
        x1=self.x_posn
        y1=self.y_posn+self.height ##변경된 y_posn의 값을 y1에 반
        x2=self.x_posn+self.width
        y2=self.y_posn      
        

        self.table.move_item(self.rect,x1,y1,x2,y2)

    def move_right(self,master):
        self.x_posn+=self.x_speed ##y_speed의 값 만큼 y_posn값을 뺌
        if(self.x_posn >=780): ##bet가 화면 하단에 걸릴때
            self.x_posn=780
        x1=self.x_posn
        y1=self.y_posn+self.height ##변경된 y_posn의 값을 y1에 반
        x2=self.x_posn+self.width
        y2=self.y_posn      
        

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
            self.height-=10##충돌이 발생하면 bet가 짧아짐
            ball.width-=1
            ball.height-=1
            print("충돌")

        if(collision):##만약 collision이 True면
            #공의 오른쪽 부분이 배트의 오른쪽부분보다 크고 ... 배트의 오른쪽에서 공이 충돌
            if((right_b>right)and(left_b<=right)and(top_b>top-r)and(bottom_b<bottom+r)):
                collision_direction="E"
                ##abs는 숫자의 부호를 제거하는 함수 속도,값을 얻는데 사용
                ##공이 배트의 어느 부분에 충돌했는지에 따라 공이 튀는 방향 바꿈.
                ball.x_speed=abs(ball.x_speed) ##공이 x의 양수값으로 (오른쪽으로 이동)
                ball.x_speed+=1 ##충돌할때마다 공의 속도가 1씩 빨라짐
                ##공의 중심이 배트의 중심에서 얼마나 먼 거리에서 충돌이 발생했는지 계산하여 y좌표값에 적용
                adjustment=(-(v_center-v_center_b))/(self.height/2)
                print(adjustment)
                ##멀리서 충돌할 수록 y는 더욱 크게 꺾임
                ball.y_speed=feel*adjustment
                

            
            elif((left_b<left)and(right_b>=left)and(top_b>top-r)and(bottom_b<bottom+r)):
                collision_direction="W"
                ball.x_speed=-abs(ball.x_speed)
                ball.x_speed-=1##반대방향으로도 1씩 빨라짐

                adjustment=(-(v_center-v_center_b))/(self.height/2)
                print(adjustment)
                ball.y_speed=feel*adjustment
    
            return(collision,collision_direction)

    ##Bet의 초기 위치값 지정
    def start_position(self):
        self.height=100
        self.x_posn=self.x_start
        self.y_posn=self.y_start
        x1=self.x_posn
        y1=self.y_posn
        x2=self.x_posn+self.width
        y2=self.y_posn+self.height
        self.table.move_item(self.rect,x1,y1,x2,y2)
