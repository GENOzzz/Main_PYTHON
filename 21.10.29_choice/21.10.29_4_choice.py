from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("400x430")
window.title("애완동물 선택하기")

##동물 투표 프로그램 생성
##myFunc정의
def myFunc():
    if var.get()==1:                                                            ##각 값에 따라 LbImg와 labelText2변경
        LbImg.configure(image=photo1)
        labelText2.configure(text="호랑이였답니다^^")
    elif var.get()==2:
        LbImg.configure(image=photo2)
        labelText2.configure(text="코끼리 였구요 ^^")
    else :
        LbImg.configure(image=photo3)
        labelText2.configure(text="야아오옹")
        
photo0=PhotoImage(file="../gif/miacat.png")                                     ##배경 설정을 위에 가장 위쪽에 배치. ##png파일로 변경시 그림판사용하면 가장 확실함.
bg=Label(window, width=400,heigh=400,image=photo0)                              ##디스플레이시 place로 하면 해당 위젯 윗층에
                                                                                ##다른위젯 배치가능

labelText=Label(window,text="좋아하는 동물 투표", fg="blue",font=("나눔고딕",20))   ##가장 상단에 text 출력

var=IntVar()
rb1=Radiobutton(window,text="고양이",variable=var,value=1,command=myFunc)
rb2=Radiobutton(window,text="강아지",variable=var,value=2,command=myFunc)
rb3=Radiobutton(window,text="사자",variable=var,value=3,command=myFunc)
button0k=Button(window,text="사진보기",command=myFunc)


photo1=PhotoImage(file="../gif/tiger1.gif")
photo2=PhotoImage(file="../gif/elf1.gif")
photo3=PhotoImage(file="../gif/lion1.gif")


LbImg=Label(window,width=200,heigh=200,bg="grey",image=photo3) ##첫 기본 LbImg 시작시 이미지를 photo3을 디폴트로.
labelText2=Label(window, text="어떤동물을 좋아하세요?")

labelText.pack(padx=5,pady=5)       ##padx>>위젯에 대한 x방향 외부패딩
bg.place(x=-0,y=-5)                            ##pady>>위젯에 대한 y방향 외부패딩
rb1.pack(padx=5,pady=5)
rb2.pack(padx=5,pady=5)
rb3.pack(padx=5,pady=5)
button0k.pack(padx=5,pady=5)
LbImg.pack(padx=5,pady=5)
labelText2.pack(padx=5,pady=5)



window.mainloop()
