import pygame,sys,time,random ##pygame 선언.
from pygame.locals import *

##전역변수 선언.
window_width=800
window_height=600

grid_size=20##1px씩 움직이면 너무 작으니까 한칸의 사이즈를 늘려주기위해 grid_size선
grid_with=window_width/grid_size#window창을 기준으로 grid_size만큼 나눠 grid_size에 맞는 가로 세로 길이 정함.
grid_height=window_height/grid_size

white=(255,255,255)
green=(10,100,20)
orange=(250,150,0)
gray=(50,50,50)

up=(0,-1)   #(y좌표만 위로)
donw=(0,1)  #(y좌표만 아래로)
left=(-1,0) #(x좌표만 왼쪽으로)
right=(1,0) #(x좌표만 오른쪽으로)

fps=10 #게임 진행 속도를 정할 fps변수.

class Snake(object):
    def __init__(self):
        self.create()
        self.color=green
    
    def create(self): #첫 생성위치.
        self.length=2 #첫 길이는 2 ##snake의 위치가 머리부터 꼬리까지 위치들(positions)임.
        self.positions=[(window_width/2,window_height/2)] #첫 위치는 가운데.
        self.direction= random.choice([up,donw,left,right]) #현재위치 + 시작하고 머리가 움직일 방향.(랜)
        
    def control(self,xy):#(xy변수를 (x,y)<좌표>로 받음)
        if(xy[0] * -1, xy[1]*-1)==self.direction:
            return#(현재 움직이는 방향의 180도 방향으론 움직이지 못함
        else:#그게 아니라면 이동가능
            self.direction=xy
            
    def move(self):
        cur=self.positions[0] #뱀의 머리
        x,y=self.direction    #자신의 현재위치
                #%window_width하면 윈도우 가로로 나눈 나머지 이므로 Snake.positions가 화면 을 넘어가게 되면 다시 0으로 돌아감.
        body =(((cur[0]+(x*grid_size))%window_width),(cur[1]+(y*grid_size))%window_height)#몸통들의 위치
        if body in self.positions[2:]:#몸통들의 위치마다 create호출 #in 시작 인덱스가 2.
            self.create()#몸통을 만들어 나감.
        else:
            self.positions.insert(0,body)#positions에 몸통을 추가함.
            if len(self.positions)>self.length: #머리가 앞으로가 이동해 자신의 길이보다 길어지면
                self.positions.pop() #꼬리를 잘라 연달아 움직이는 것 처럼 보이는
                
    def eat(self): #길이가 길어지는 eat함수.
        self.length+=1
        
    def draw_snake(self,surface):#화면에 뱀을 그려주는 draw
        for p in self.positions:
            draw_apple(surface,self.color,p)
            
class Apple(object):#class Apple
    def __init__(self):
        self.position=(0,0) #한칸만 차지
        self.color=orange

    def create(self): #위치는 랜덤으로 생
        self.position=(random.randint(0,grid_with-1)*grid_size,random.randint(0,grid_height-1)*grid_size)
    
    def draw(self,surface):#화면에 표시하기위한 draw
        draw_apple(surface,self.color,self.position)    
        
        
def draw_apple(surface,color,pos):
    r=pygame.Rect((pos[0],pos[1]),(grid_size,grid_size))
    pygame.draw.rect(surface,color,r)
        
def check_eat(Snake,Apple): #(Snake와 Apple 객체를 변수로 받는)
    if Snake.positions[0]==Apple.position:
        Snake.eat()
        Apple.create()     

def show_info(length,speed,surface):
    font = pygame.font.Font(None,34)
    text = font.render("      Length : "+str(length)+"        Speed : "+str(round(speed,2)),2,gray)
    pos = text.get_rect()
    pos.centerx=150
    surface.blit(text,pos)  

# if __name__=='__main__' >> 해당모듈이 인터프리터에서 직접 실행된 경우만 if문 이하의 코드를 실행하라.
#그 외 모듈화 하여 import시켜 사용하게되면 else구문도 만들어 주어야함.
#__name__ 이란 인터프리터가 실행되기전에 만들어둔 글로벌 변수.
if __name__ == '__main__' :
    snake=Snake()
    apple=Apple()
                                            
    pygame.init() ##pygame 초기화  #set_mode (size = (0, 0), flags = 0, depth = 0, display = 0, vsync = 0)
    window=pygame.display.set_mode((window_width,window_height))
    pygame.display.set_caption("self_snake")#타이틀바의 텍스트 설정.
    surface = pygame.Surface(window.get_size())#현재 설정된 디스플레이 표면에 대한 참조를 가져옴.
                                #Surface란 모든 2D객체,색이나 이미지를 가지는 빈 시트를 일컫는 말.
    surface = surface.convert()#이미지의 픽셀 형식을 변경?
    surface.fill(white)
    clock = pygame.time.Clock()#화면을 초당 몇 번 출력하는가를 설정하기위해 선언
    pygame.key.set_repeat(1,40)#누르고 있는키의 반복을 제어 #set_repeat(지연시간,간격) 단위는 밀리초.
    window.blit(surface,(0,0))#blit() 다른 Surface객체를 자신에게 그려넣는 함수(복사한다 생각)
                                        
    
    while True:
                        #event를 담당하는 모듈 event
        for event in pygame.event.get(): #event.get()은 게임의 이벤트 큐에 있는 모든 이벤트를 순서열로 반환.
            if event.type == QUIT:#게임종료버튼 창닫기버튼.
                pygame.quit()
                sys.exit() ##조정하는 부분.
            elif event.type==KEYDOWN: #KEYDOWN type의 이벤트 발생시.(키보드 입력)
                if event.key==K_UP:    #위 방향키 일경우
                    snake.control(up)  #snake객체의 control(up) 호출
                elif event.key==K_DOWN:
                    snake.control(donw)
                elif event.key==K_LEFT:
                    snake.control(left)
                elif event.key==K_RIGHT:
                    snake.control(right)
                    
        surface.fill(white) #화면에 색상 채우기.
        snake.move()
        check_eat(snake,apple)
        speed=(fps+snake.length)/2
        show_info(snake.length,speed,surface)
        snake.draw_snake(surface)
        apple.draw(surface)
        window.blit(surface,(0,0))
        pygame.display.flip()#전체 디스플레이 화면을 업데이트
        pygame.display.update()#소프트웨어 디스플레이 화면 일부 업데이트
        clock.tick(speed)##위에서 설정한 clock,tick()함수를 통해 초당 프레임 정함.
