from tkinter import *


window=Tk()
window.title("PNG_PONG")


##화면설계 : 기본 바탕이될 공,배트,배경 생성.
###캔버스 생성
canvas=Canvas(window,width=800,height=500,bg="teal")
canvas.pack()

##캔버스 위에 선 생성
canvas.create_line(400,0,400,500, width=2,fill="snow",dash=(20,30))
                  #x1,y1,x2,y2 좌표 선의 굵기 색상 길이와 빈공간
###캔버스 위에 공 생성
canvas.create_oval(388,238,412,262,fill="gold")

###캔버스 위에 배트 생성
canvas.create_rectangle(20,200,40,300,fill="tomato")
canvas.create_rectangle(760,200,780,300,fill="dodgerblue")

window.mainloop()    
