from tkinter import *

btnList=[None]*9

fnameList=["../gif/puz1.gif"] ##동일한 레벨의 폴더위치는 ../(상위폴더)으로 나간뒤 해당폴더로 들어가야함

for i in range(8):      ##i는 0부터 8-1까지 반복
    fnameList.append("../gif/puz"+str(i+2)+".gif")##하는동안 fnameList배열에 ()내용을 추가;

photoList=[None]*9 ##9칸짜리 photoList배열 생성

i,k=0,0
xPos,yPos=0,0
num=0

window = Tk()
window.geometry("210x210")

for i in range(9):  ##i는 0부터 9-1까지 반복
    photoList[i]=PhotoImage(file=fnameList[i])  ##photoList배열의 i번째의 flie은 fname배열의 i번째로대입
    btnList[i]=Button(window, image=photoList[i])##btn배열의 i번째에 위젯 생성. image는 photo배열의i번째
         
for x in range (3) :    
               
    for y in range(3):  
        btnList[num].place(x=xPos,y=yPos)    ##btn배열의 num번째 의 플레이스 지정<<<디스플레이            
        xPos+=70                                      
        num+=1
    xPos=0  
    yPos+=70                                         
      
window.mainloop()

