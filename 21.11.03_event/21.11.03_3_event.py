from tkinter import *
from tkinter import messagebox

##EVENT 처리 <<< 사용자로부터 키보드나 마우스의 입력이 발생한 경우를 EVENT라고함.

def clickLeft(event):                   ##이벤트 발생시 함수정의 (clickLeft)
    messagebox.showinfo("마우스","왼쪽")##이벤트 발생하면(함수 실행시) 마우스창에 왼쪽이라는 텍스트 출력
    
def clickRight(event):                  ##이벤트 발생시 함수정의 (clickRight)
    messagebox.showinfo("마우스","오른쪽")##함수 실행시 마우스창에 오른쪽이라는 텍스트 출력
    
def clickImage(event):                  ##이벤트 발생시 함수정의 (clickImage)
    messagebox.showinfo("그림","그림 위에서 버튼이 클릭됨")##그림창에 그림위에~텍스트 출력

def overImage(event):                   ##함수정의 overImage
    messagebox.showinfo("그림","그림위에 마우스를 올리셨군요?")##그림창에 그림위에~텍스트 출력

def clickMouse(event):      ##clickMouse 함수정의 
    txt=""
    if event.num==1:        ##event값이 1이면
        txt+="마우스 왼쪽버튼이 ("##마우스 왼쪽버튼이 출력
    elif event.num==2:      ##2이면
        txt+="마우스 가운데버튼이("##마우스 가운데 버튼이 출력
    elif event.num==3:      ##3이면
        txt+="마우스 오른쪽버튼이 ("##마우스 오른쪽 버튼이 출력

    txt+=str(event.x)+","+str(event.y)+")에서 클릭됨" ##event.x값 event.y값 출력
    label1.configure(text=txt)                       ##해당 출력이 text에 대입
    label1.place(x=event.x,y=event.y)                ##발생시 위치에 따라 출력위치 변경
  
btnList=[None]*9

photoList=[None]*9 

i=0
xPos,yPos=0,0

window = Tk()
window.geometry("300x300")

label1=Label(window,text="이곳이 바뀜")
        
for x in range (3) :    
    xPos=0
    
    for y in range(3):        
        photoList[i]=PhotoImage(file="../gif/puz"+str(i+1)+".gif")
        btnList[i]=Button(window, image=photoList[i])             
        btnList[i].place(x=xPos,y=yPos)
        xPos+=70                                      
        i+=1
    yPos+=70

for i in range(9):
    btnList[i].bind("<Button>",clickImage) ##마우스 공통버튼을 클릭했을 때 이벤트 코드 : <Button>
'''
for i in range(9):
    btnList[i].bind("<Enter>",overImage) ##마우스를 이미지위에 올렸을때 이벤트 코드 : <Enter>
'''
window.bind("<Button>",clickMouse)
'''
window.bind("<Button-1>",clickLeft) ##마우스 왼쪽 버튼을 클릭했을 때 이벤트 코드 : <Button-1>

window.bind("<Button-3>",clickRight) ##마우스 오른쪽 버튼을 클릭했을 때 이벤트 코드 : <Button-3>
'''


label1.pack(anchor=CENTER)

window.mainloop()
