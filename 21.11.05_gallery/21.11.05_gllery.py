from tkinter import *
from tkinter import messagebox
from time import *

##gallery
##EVENT 처리 <<< 사용자로부터 키보드나 마우스의 입력이 발생한 경우를 EVENT라고함.
picList=[]

picList1=[]  ##사진의 이름을 담고있는 배열 선언
for i in range (22):
    if i<13:
        picList.append("jeju"+str(i+1))

    elif i >=13:
        picList.append("pic"+str(i-12))



'''
for i in range (13):
    picList1.append("jeju"+str(i+1))
    
picList2=[]  ##다른 사진의 이름을 담고있는 배열 선언
for i in range(9):
    picList2.append("pic"+str(i+1))
'''
    
button=["../gif/Nextbutton1.png","../gif/Prevbutton1.png","../gif/arrow1.png","../gif/arrow2.png"] ## 버튼용 이미지 정보 생성

  
num=0
page=0

##사진을 넘기고 되돌리는 함수 선언
def clickNext():
    global num  ##변수 num을 전역변수로 선언
    num+=1      ##해당 함수실행시 num값에 +1
    if num>21:  ##num값이 12보다 커진다면(사진리스트보다 커진다면)
        num=0   ##num은 0으로 <<< 리스트의 0번째를 호출하기 위함
    photo=PhotoImage(file="../gif/"+picList[num]+".gif") ##PhotoImage(file은 pic리스트의 num번째로 변경)
    pLabel.configure(image=photo)       ##p.Label을 바꿔라 photo로 <<<위에서 변경된 photo
    pLabel.image=photo  ##pLabel(window, image=photo)의 photo도 바뀐 photo로
    Text.configure(text=picList[num])

def clickNext2():
    global num
    num+=2
    if num>21:
        num=0
    photo=PhotoImage(file="../gif/"+picList[num]+".gif")
    pLabel.configure(image=photo)
    pLabel.image=photo
    Text.configure(text=picList[num])

def clickPrev(): ##Next의 반대 버전 함수.
    global num
    num-=1
    if num<0:
        num=21
    photo=PhotoImage(file="../gif/"+picList[num]+".gif")
    pLabel.configure(image=photo)
    pLabel.image=photo
    Text.configure(text=picList[num])

def clickPrev2():
    global num
    num-=2
    if num<0:
        num=21
    photo=PhotoImage(file="../gif/"+picList[num]+".gif")
    pLabel.configure(image=photo)
    pLabel.image=photo
    Text.configure(text=picList[num])

def Nextpage(): ##화살표 위쪽을 누르면 다른 리스트의 사진을 보여주는 함수
    global num
    num+=13
    if num>21:
        num=0
    photo=PhotoImage(file="../gif/"+picList[num]+".gif")
    pLabel.configure(image=photo)
    pLabel.image=photo
    Text.configure(text=picList[num])

'''
    global page
    page+=1   ##해당 함수가 호출되면 page +1을 해주고
    if page>1:  ##page가 1보다 크다면 즉 2가 된다면 page는 다시 0으로 돌아간다.
        page=0
    if page==1: ##만약 page가 1이라면
        if num<13:
            num+13
            photo=PhotoImage(file="../gif/"+picList[num-13]+".gif") ##적당한 List2의 사진을 불러온다.
            Text.configure(text=picList[num-13])
        pLabel.configure(image=photo)
        pLabel.image=photo
            
    if page==0: ##page가 0이되면            ##List1의 num번째 사진을 불러온다
        if num>=13:                                  ##picList의 사진을 불러온다
            num-13
            photo=PhotoImage(file="../gif/"+picList[num]+".gif")
            Text.configure(text=picList[num])
        photo=PhotoImage(file="../gif/"+picList[num]+".gif")
        pLabel.configure(image=photo)
        pLabel.image=photo
        Text.configure(text=picList[num])
'''
##이벤트 발생시 사진을 넘기고 되돌리는(clickNext,Prev) 함수를 호출하는 함수 선언 및 
def pageUp(event):
    clickNext()

def pageDown(event):
    clickPrev()

def pageUp2(event):
    clickNext2()

def pageDown2(event):
    clickPrev2()

def pageChange(event):
    Nextpage()

window = Tk()
window.geometry("900x600")
window.title("사진 앨범 보기")

myBG=PhotoImage(file="../gif/sky1.png") ##배경용 이미지 정보 생성
bg=Label(window,width=900,heigh=600,image=myBG)

##키보드이벤트 발생시 함수호출
window.bind("<Right>",pageUp)
window.bind("<Left>",pageDown)
window.bind("<Prior>",pageUp2)
window.bind("<Next>",pageDown2)
window.bind("<Up>",pageChange)

##버튼 이미지 위젯 생성
nextImage=PhotoImage(file=button[0])
prevImage=PhotoImage(file=button[1])
next2Image=PhotoImage(file=button[2])
prev2Image=PhotoImage(file=button[3])

##버튼 위젯 생성
btnPrev=Button(window, image=prevImage,cursor="cross",command=clickPrev) ##해당 위젯을 누르면 clickPrev를 호출함
btnNext=Button(window, image=nextImage,cursor="heart",command=clickNext) ##cursor 명령어는 cursor의 모양을 제어
btnPrev2=Button(window, image=prev2Image,cursor="wait",command=clickPrev2)
btnNext2=Button(window, image=next2Image,cursor="Arrow",command=clickNext2)
btnUp=Button(window, text="◎",command=Nextpage)

##라벨 위젯 생성
Text=Label(window, text=picList[0], font=("나눔고딕",30), fg="skyblue", border=0)

##이미지 정보 생성
photo=PhotoImage(file="../gif/"+picList[0]+".gif")

##이미지 위젯 생성
pLabel=Label(window, image=photo)

##위젯 디스플레이
bg.place(x=0,y=0)
btnUp.place(x=445,y=15)
btnPrev.place(x=365,y=6)
btnNext.place(x=500,y=6)
btnPrev2.place(x=200,y=6)
btnNext2.place(x=600,y=6)
pLabel.place(x=120,y=70)
Text.place(x=650,y=530)

window.mainloop()
