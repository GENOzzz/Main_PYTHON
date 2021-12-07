#20211006 윈도우 프로그래밍, 그림판 만들기_박현호#

#윈도우 프로그래밍을 하기 위해 tkinter 모듈 가져오기

from tkinter import* #*는 모든 것을 뜻하는 명령어

##변수 선언##
window=None #창의 정보를 저장할 수 있는 변수 생성 #None은 설정값 없이 초기값으로 하겠다는 뜻
canvas=None #캔버스의 정보를 저장할 수 있는 변수 생성
x1, y1, x2, y2=None,None,None,None #x1=None
                                                       #y1=None
                                                       #x1=None
                                                       #y2=None
                    #선의 시작점과 끝점의 정보(x,y좌표값)를 저장할 수 있는 변수 생성
##함수선언부##
 #마우스를 클릭을  눌렀을 때 실행할 사용자 정의 함수 선언
def MC(event):  #키보드 및 마우스를 누르는 것을 event라고 함 #함수 들여쓰기 확실히 할것-Python만 가진 특징
    global x1, y1, x2, y2 #global = 전역변수 선언(ex 전교회장)    #다른 프로그램은 {  }를 사용
    x1=event.x
    y1=event.y
 #마우스를 클릭을 땠을 때 실행할 사용자 정의 함수 선언
def MD(event): 
    global x1, y1, x2, y2
    x2=event.x ##복사 붙여넣기 할때 숫자 확인하기 x1 x2 y1 y2//
    y2=event.y
    canvas.create_line(x1, y1, x2, y2, width=4, fill="black")
##메인코드##
window=Tk()#창 생성 #Tk=윈도우 창 베이스 같은 느낌
#window2=Tk()
window.title("유사 그림판")#생성된 창(window=내가 정한 코딩용 이름)의 제목(프로그램 위에 뜰 이름) 지정
#window.title("유사그림판2") -> 창을 여러개 생성가능 - 객체지향적.
canvas=Canvas(window,height=800,width=800)#생성된 창(window)에 그림을 그릴 수 있는 캔버스 생성 #Python은 대소문자 가림
canvas.bind("<Button-1>",MC)#bind()함수로 event와 함수를 연결
canvas.bind("<ButtonRelease-1>",MD)
canvas.pack()#화면에 캔버스 디스플레이
window.mainloop()#창에 계속해서 event가 발생하고 있는지 검토하는 함수
