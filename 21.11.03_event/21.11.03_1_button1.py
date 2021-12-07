from tkinter import *
window=Tk()

window.geometry("800x600")

'''
##버튼생성
button1=Button(window, text=" 버튼1 ")
button2=Button(window, text=" 버튼2 ")
button3=Button(window, text=" 버튼3 ")
button4=Button(window, text=" 버튼4 ")
button5=Button(window, text=" 버튼5 ")
button6=Button(window, text=" 버튼6 ")
button7=Button(window, text=" 버튼7 ")
button8=Button(window, text=" 버튼8 ")
button9=Button(window, text=" 버튼9 ")
button10=Button(window, text="버튼10")
button11=Button(window, text="버튼11")
button12=Button(window, text="버튼12")

##버튼출력
button1.place(x=0,y=0)
button2.place(x=50,y=0)
button3.place(x=100,y=0)
button4.place(x=0,y=30)
button5.place(x=50,y=30)
button6.place(x=100,y=30)
button7.place(x=0,y=60)
button8.place(x=50,y=60)
button9.place(x=100,y=60)
button10.place(x=0,y=90)
button11.place(x=50,y=90)
button12.place(x=100,y=90)

'''
##반복문을 이용하여 button생성하기.
button=[None]*20 ##위젯을 담을 배열 button생성
xPos,yPos=0,0    ##button[0]번째의 위치 설정을 위한 초기값생성
i=0              ##위젯Button의 이름과 배열button의 자리를 찾기위한 i 생성
for x in range (5) :    ##x가 5번도는동안
    xPos=0              ##xPos는 0부터 시작
    for y in range(4):  ##y가 4번 도는동안
        button[i]=Button(window,text="버튼"+str(i+1)) ##배열button의 i번째 자리에 위젯생성
        button[i].place(x=xPos,y=yPos)                ##button[i]자리의 위젯 플레이스 설정
        xPos+=50                                      ##다음 위젯의 x값 설정
        i+=1                                          ##다음 자리를 찾기위해 i+=1
    yPos+=30                                          ##y for문<<<가로배치가 끝나면 이동시켜주기위해 +30
      
window.mainloop()


