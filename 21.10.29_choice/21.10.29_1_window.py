from tkinter import *       ##tkinter 라이브러리를 import 하는데 * <-모든것을
from tkinter import messagebox

##Tk()는 기본이 되는 윈돌우를 반환
                                        ##루트 윈도우(Root Window)또는 베이스윈도우(Base Window)라고 부름.
window=Tk()                 ##window선언 Tk()클래스로부터
                                     

##윈도우창에 제목표시
window.title("연습용 창")

##윈도우창의 초기 크기 지정
window.geometry("1000x900")  ### *대신 x사용

##창크기 변경 가능 여부 정#0또는 1로도 가능
window.resizable(width=TRUE, height=1)

##위젯(윈도우 창에 나올 수 있는 문자,버튼,체크박스, 라디오버튼 등
##위젯은 생성하고 디스플레이해야 화면에 표시. 2터치로 진행
##Label은 문자 또는 이미지를 표현할수 있는 위젯
##Label생성
label1=Label(window, text="SWEDU~~ PYTHON을")
                                    ##text는 글자 자체
label2=Label(window, text="열심히", font=("궁서체",30), fg="blue")
                                                                ##font는 글꼴과 크기  #fg는 foregruond =글자색
label3=Label(window, text="HOME",bg="magenta",width=10,height=5)
                                                                        ##bg는 background = 배경색  ##width,height=위젯의 폭과 높이
                                                                        ##anchor는 위젯의 어느 위치에 글자를 배치시킬지
                                                                        ##N,NE,E,SE,S,SW,NW,CENTER등 기본값은 CENTER
                                                                        ##north,east,south,west

##Label위젯을 pack()함수를 통해 화면에표시
label1.pack()
label2.pack()
label3.pack()

##이미지 표시(이미지 디스플레이는 3터치로 진행

##1.이미지생성
photo3=PhotoImage(file="../gif/jeju1.gif")  ##이미지를 배경으로깔고 싶으면 생성을 먼저시켜 먼저 배치(포토샵 레이아웃 생각-순서변경 임의로 불가;)
photo=PhotoImage(file="../gif/jeju10.gif")                               ##가장 아래 깔아배경처럼 보이게 만듦.
photo2=PhotoImage(file="../gif/cat2.gif")

##2.라벨 위젯을 생성(해당 라벨에 이미지 삽입)

imglable=Label(window,image=photo)
imglable3=Label(window,image=photo3, width=370)
imglable2=Label(window,image=photo2)

##3.라벨위젯을 화면에 표
imglable.pack(side=RIGHT)   ##pack(순서에 맞게 띄우고 정렬)
imglable2.pack(side=LEFT)
imglable3.place(x=-2,y=-2)  ##place(좌표설정)

##button생성 및 표시 ==2터치

#버튼 생성	                                ##command=함수명==> 함수옆()필요없음.
button1=Button(window, image = photo2, command=quit)

#버튼표시
button1.place(x=750,y=70)

##버튼에 사용자 함수기능 삽입
def myFunc():
    messagebox.showinfo("고양이버튼","야아아옹")


button2=Button(window, image = photo2, command=myFunc)
button2.place(x=300,y=500)
    


#이 부분에서 화면을 구성하고 처리
window.mainloop() 




