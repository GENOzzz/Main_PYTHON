from tkinter import*
from tkinter import messagebox
window=Tk()
##체크박스
#함수정의
def myFunc():
    if chk.get()==0:##0=FALSE >> 체크가 안됐을시
        messagebox.showinfo("","체크버튼이 꺼졌어요")
    else:                 ##그외 >> 체크가 됐을시
        messagebox.showinfo("","체크버튼이 켜졌어요")
##메인코드부분
chk=IntVar()
##체크박스 버튼 생성
cb1=Checkbutton(window, text="클릭하세요",variable=chk,command=myFunc)
##체크박스 디스플레이
cb1.pack()

##라디오 버튼
#함수정의
def myFunc1():
    if var.get()==1:        ##var값이 1이면
        label1.configure(text="PYTHON")##configur2 >> 내용을 바꾸겠다.
    elif var.get()==2:      ##var값이 2라면
        label1.configure(text="C++")
    else:                       ##그외 1,2,빼고
        label1.configure(text="JAVA")
##메인코드부분
var=IntVar()
##3개의 라디오 버튼 준비.
                                     ##radiobutton에 variabel=변수명 설정
rb1=Radiobutton(window,text="PYHON",variable=var,value=1,command=myFunc1)
                                        ##rb1을 선택하면 var라는 변수에 value=1 이 myfunc1로 넘어감
rb2=Radiobutton(window,text="C++",variable=var,value=2,command=myFunc1)
                                                                        ##2가 넘어감
rb3=Radiobutton(window,text="JAVA",variable=var,value=3,command=myFunc1)
                                                                        ##3이 넘어감
label1=Label(window,text="선택한 언어 : ",fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

window.mainloop()
