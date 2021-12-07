###imagebutton 의 for문 갯수 줄이기
from tkinter import *

btnList=[None]*9

photoList=[None]*9 

i=0
xPos,yPos=0,0

window = Tk()
window.geometry("210x210")

        
for x in range (3) :    
    xPos=0
    
    for y in range(3):        
        photoList[i]=PhotoImage(file="../gif/puz"+str(i+1)+".gif")##photo배열로 이미지 생성 바로.
        btnList[i]=Button(window, image=photoList[i])             ##버튼 위젯 (이미지를 갖는)생성
        btnList[i].place(x=xPos,y=yPos)                          ##버튼 위젯 디스플레이(place)로.
        xPos+=70                                      
        i+=1
    yPos+=70

window.mainloop()
