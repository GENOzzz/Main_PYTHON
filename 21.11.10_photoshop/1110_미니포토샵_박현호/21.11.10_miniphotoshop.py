
##미니포토샵
##포토샵과 같은 소프트웨어를 "영상처리(Image Processing)프로그램" 이라함
##원칙적으로 영상처리에 대한 이론과 알고리즘을 익힌 후 미니 포토샵 프로그램을 작성하면좋음
##현실적으로 이론 배제 - 화면에 구현되는 것 위주로 진행

##주의사항 1.이미지 파일명이나 저장된 경로에 한글들어가면 안됨.
##주의사항 2. 이미지는 가로와 세로크기가 동일해야함.
##주의사항 3. 처리하는 속도가 다소 오래걸림

#사용할 라이브러리 또는 모듈을 임포트
from tkinter import *
#파일 입출력을위한 모듈
from tkinter.filedialog import *
#숫자나 문자를 입력받기 위한 모듈
from tkinter.simpledialog import *
#이미지매직(외부라이브러리) 모듈
#gif뿐 아니라 jpg,png같은 이미지를 모두 처리하기위함.
from wand.image import *
from wand.drawing import Drawing
from wand.image import Image

###함수가 공통으로 사용할 변수 선언부분
window,canvas,paper=None,None,None
photo,photo2=None,None
oriX,oriY,newX,newY=0,0,0,0

###함수정의부-각메뉴를 선택할때 실행될 함수 선언.

#open함수선언
def displayImage(img,width,height):
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if canvas!=None:
        canvas.destroy() ##기존에 캔버스가 있었다면 이미지가 새캔버스위에 그려지는데 헌캐버스보다 아래에 그려
    #새 캔버스 생성,처리된 이미지의 가로 세로 사이즈대로 생성,,Canvas는 내장함수
    #캔버스 흰테두리 없애기 ,bd=0,higlightthickness=0
    canvas=Canvas(window, width=width, height=height,bd=0,highlightthickness=0)
    #새 캔버스에 붙일 paper생성 처리된 이미지의 가로세로 사이즈대로 생성
    paper=PhotoImage(width=width,height=height)
    #캔버스에 페이퍼를 붙이는 작업. 그후 위에 처리된 이미지 출력
    #생성될 페이퍼의 위치는 캔버스의 가로세로 사이즈의 중간위치
    canvas.create_image((width/2,height/2),image=paper,state="normal")

    #새캔버스와 종이 위에 처리된 이미지 출력
    #make_blob(format=none)은 이미지를 바이너리 코드로 변환해 주는 함수;벼열의 형태로 저장
    #흰종이에 사진을 출력하기 위해 이미지 파일의 모든점(픽셀)에 접근
    blob=img.make_blob(format='RGB')
    for i in range(0,width):
        for k in range(0,height):
            r=blob[(i*3*width)+(k*3)+0]
            g=blob[(i*3*width)+(k*3)+1]
            b=blob[(i*3*width)+(k*3)+2]
            paper.put("#%02x%02x%02x"%(r,g,b),(k,i))

    canvas.pack(expand=1,anchor=CENTER)

###파일불러오기####    
def func_open(): ##전역변수선언.
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    readFp=askopenfilename(parent=window, filetypes=(("모든 그림파일","*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),("모든파일","*.*")))
    #photo는 처음 불러들인 원본 이미지
    photo=Image(filename=readFp)
    oriX=photo.width #원본이미지의 가로사이즈 oriX에 저장
    oriY=photo.height#원본이미지의 세로사이즈 oriY에 저장
    ##처리 결과를 저장할 변수 photo2
    photo2=photo.clone() #wand.image에서 제공하는함수 clone() <<< 원본이미지를 복제하여 photo2에 저장.
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY) #화면에 이미지를 출력하는 함수 호출<<displayImage() 생성해야
    
    
###사진저장###
def func_save():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2==None:
        return ##캔버스 destroy를 응용하여 photo2가 없으면 return으로 함수 빠져나감
    
    saveFp=asksaveasfile(parent=window,mode="w",defaultextension=".jpg",
                         filetypes=(("JPG파일","*.jpg;*.jpeg"),("모든파일","*.*")))
    savePhoto=photo2.convert("jpg")
    savePhoto.save(filename=saveFp.name)

####원본으로되돌리기####
def func_origin():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    if photo==None:
        return
    displayImage(photo,oriX,oriY)

#####프로그램종료####
def func_exit():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    window.quit()
    window.destroy()

#####사진확대####
def func_zoomin():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    
    if photo2 == None:
        return
    #askinteger <<사용자로부터 정수값을 입력받음.    
    scale=askinteger("확대배수","확대할 배수를 입력하세요(2~4)",minvalue=2,maxvalue=4)##사용자로부터 입력받은 값을 scale에 저장
    photo2.resize(int(newX*scale),int(newY*scale))
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)
    

    
####사진축소####
def func_zoomout():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
   
    if photo2 == None:
        return
        
    scale=askinteger("축소배수","축소할 배수를 입력하세요(2~4)",minvalue=2,maxvalue=4)
    photo2.resize(int(newX/scale),int(newY/scale))
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)
    

####사진 상하반전####
def func_flip():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    
    if photo2 == None:
        return
    
    photo2.flip()
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)
    
####사진 좌우반전####
def func_flop():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    
    if photo2 == None:
        return
    
    photo2.flop()
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

#사진회전
def func_rotate():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    
    if photo2 == None:
        return
    
    degree=askinteger("회전","회전할 각도를 입력하세요 (0~360)",minvalue=0,maxvalue=360)
    photo2.rotate(degree)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)
    
    
####사진밝게####   
def func_bright():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
    
    value=askinteger("밝게","값을 입력하세요(100~200)",minvalue=100,maxvalue=200)
    photo2=photo.clone()
    photo2.modulate(value,100,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)
    
####사진어둡게####
def func_dark():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
    
    value=askinteger("어둡게","값을 입력하세요(0~100)",minvalue=0,maxvalue=100)
    photo2=photo.clone()
    photo2.modulate(value,100,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

##사진채도조절##
def func_inversion():
    pass
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
    
    value=askinteger("채도","값을 입력하세요(0~100)",minvalue=0,maxvalue=100)
    photo2=photo.clone()
    photo2=photo.clone()
    photo2.modulate(100,100,value)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

####사진선명하게####
def func_clear():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
    
    value=askinteger("선명하게","값을 입력하세요(100~200)",minvalue=100,maxvalue=200)
    photo2=photo.clone()
    photo2.modulate(100,value,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

####사진탁하게####    
def func_unclear():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
    
    value=askinteger("탁하게","값을 입력하세요(0~100)",minvalue=0,maxvalue=100)
    photo2=photo.clone()
    photo2.modulate(100,value,100)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)
    
####사진흑백####
def func_mono():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    
    if photo2 == None:
        return
    
    photo2.type="grayscale"
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

####사진에 글상자 삽입####
def func_text():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return

    

###메인코드부분
window=Tk()
window.geometry("900x600")
window.title("미니 포토샵(Ver_0.1)")

##배경이미지생성
mybg=PhotoImage(file="backgr.png")
bg=Label(window,width=1000,heigh=1000,image=mybg)
bg.place(x=0,y=-200)


#메뉴생성
##1.메뉴자체생성 및 화면에 디스플레이
##메뉴자체이름=Menu(부모window)
##부모윈도우.config(menu=메뉴자체이름
mainMenu=Menu(window)
window.config(menu=mainMenu)



'''
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack( expand=1, anchor=CENTER)
'''


##2.상위메뉴생성
#상위메뉴이름=Menu(메뉴자체이름)
#메뉴자체이름.add_cascade(label="상위메뉴텍스트",=상위메뉴이름)
##add_cascade()메소드는 메뉴자체와 상위메뉴를 연결
fileMenu=Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="FILE",menu=fileMenu)

##3.하위메뉴생성
#상위메뉴이름.add_command(label="하위메뉴이름",command=함수명)<<<함수는 클릭할때 호출하게됨
#add_command()메소드는 하위 메뉴 항목 생성
fileMenu.add_command(label="OPEN",command=func_open)
fileMenu.add_command(label="SAVE",command=func_save)
fileMenu.add_separator()##구분선 삽입
fileMenu.add_command(label="ORIGINAL",command=func_origin)
fileMenu.add_separator()
fileMenu.add_command(label="EXIT",command=func_exit)
#추가 상위메뉴생성
imageMenu1=Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="IMAGE_1",menu=imageMenu1)
#추가 상위메뉴속 하위메뉴생성
imageMenu1.add_command(label="ZOOM_IN",command=func_zoomin)
imageMenu1.add_command(label="ZOOM_out",command=func_zoomout)
imageMenu1.add_separator()
imageMenu1.add_command(label="FLIP",command=func_flip)
imageMenu1.add_command(label="FLOP",command=func_flop)
imageMenu1.add_separator()
imageMenu1.add_command(label="ROTATE",command=func_rotate)
#추가2 상위메뉴생성
imageMenu2=Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="IMAGE_2",menu=imageMenu2)
#추가2 상위메뉴 속 하위메뉴 생성
imageMenu2.add_command(label="BRIGHT",command=func_bright)
imageMenu2.add_command(label="DARKNESS",command=func_dark)
imageMenu2.add_separator()
imageMenu2.add_command(label="COLOR_INVERSION",command=func_inversion)
imageMenu2.add_separator()
imageMenu2.add_command(label="CLEAR",command=func_clear)
imageMenu2.add_command(label="UNCLEAR",command=func_unclear)
imageMenu2.add_separator()
imageMenu2.add_command(label="MONO",command=func_mono)

#추가3 상위메뉴 생성
imageMenu3=Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="IMAGE_3",menu=imageMenu3)
#추가3 상위메뉴 속 하위메뉴 생성
imageMenu3.add_command(label="TEXT",command=func_text)




window.mainloop()
