##이미지 정렬
from tkinter import *

window=Tk()
window.geometry("800x600")

##이미지위젯표시
img1=PhotoImage(file="../gif/puz1.gif")
imglb1=Label(window,image=img1)
imglb1.pack(side=LEFT)

img2=PhotoImage(file="../gif/puz2.gif")
imglb2=Label(window,image=img2)
imglb2.pack(side=LEFT)

img3=PhotoImage(file="../gif/puz3.gif")
imglb3=Label(window,image=img3)
imglb3.pack(side=LEFT)

##반복문과 리스트를 결합하여 이미지 위젯을 순서대로 표시
#리스트 선언
img=[None]*10
imglb=[None]*10

#반복하여 위젯 생성
for i in range(1,10):
    img[i]=PhotoImage(file="../gif/puz"+str(i)+".gif")  ##문자열 사이에 변수를 추가하고 싶을때str으로 문자로바꿔 받을것.
    imglb[i]=Label(window,image=img[i])
    imglb[i].pack(side=RIGHT)

window.mainloop()

