from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *
from wand.drawing import Drawing
from wand.image import Image
from wand.color import Color
import tkinter as tk
import tkinter.font as tkFont

window,canvas,paper=None,None,None
photo,photo2,photo3=None,None,None
oriX,oriY,newX,newY=0,0,0,0
x1,y1,x2,y2=None,None,None,None

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
    
    ##format='png'방식으로 처리할경우 이미지 처리시간이 빨라짐. 투명한 배경지원(사진 회전시에도 검은배경 안나옴)
    blob=img.make_blob(format='png')
    paper.put(blob)

    #캔버스에 페이퍼를 붙이는 작업. 그후 위에 처리된 이미지 출력
    #생성될 페이퍼의 위치는 캔버스의 가로세로 사이즈의 중간위치
    canvas.create_image((width/2,height/2),image=paper,state="normal")


    '''
    #새캔버스와 종이 위에 처리된 이미지 출력
    #make_blob(format=none)은 이미지를 바이너리 코드로 변환해 주는 함수;벼열의 형태로 저장
    #흰종이에 사진을 출력하기 위해 이미지 파일의 모든점(픽셀)에 접근 >>처리시간이 엄청 오래걸림.
    blob=img.make_blob(format='RGB')
    for i in range(0,width):
        for k in range(0,height):
            r=blob[(i*3*width)+(k*3)+0]
            g=blob[(i*3*width)+(k*3)+1]
            b=blob[(i*3*width)+(k*3)+2]
            paper.put("#%02x%02x%02x"%(r,g,b),(k,i))
    '''

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
    ###화면에 파일이름출력###
    string=readFp
    p=string.split('/')
    s=len(p)
    '''
    print(string)
    print(p)
    print(s)
    '''
    fontStyle=tkFont.Font(family="Lucida Grande",size=20)
    photo_title.configure(text=p[s-1],bg="black",font=fontStyle)
    
    fileMenu.entryconfig("SAVE", state="normal")
    fileMenu.entryconfig("ORIGINAL", state="normal")
    fileMenu.entryconfig("WORTERMARK", state="normal")
    fileMenu.entryconfig("CLOSE", state="normal")
    fileMenu.entryconfig("MARK_IN", state="normal")
    mainMenu.entryconfig("IMAGE_1", state="normal")
    mainMenu.entryconfig("IMAGE_2", state="normal")
    mainMenu.entryconfig("IMAGE_3", state="normal")

def func_close():
    global window,canvas, paper, photo, photo2,photo3, oriX, oriY
    if photo2==None:
        return
    canvas.destroy()
    photo_title.configure(text="",bg="gray")

    fileMenu.entryconfig("SAVE", state="disable")
    fileMenu.entryconfig("ORIGINAL", state="disable")
    fileMenu.entryconfig("WORTERMARK", state="disable")
    fileMenu.entryconfig("CLOSE", state="disable")
    fileMenu.entryconfig("MARK_IN", state="disable")
    mainMenu.entryconfig("IMAGE_1", state="disable")
    mainMenu.entryconfig("IMAGE_2", state="disable")
    mainMenu.entryconfig("IMAGE_3", state="disable")
    
    
###워터마크 이미지지정###
def func_watermarkopen():
    global window,canvas, paper, photo, photo2,photo3, oriX, oriY
    readFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),  ("모든 파일", "*.*") ))
    photo3 = Image(filename=readFp)


###워터마크 이미지 삽입###
def func_watermark() :
    global window,canvas, paper, photo, photo2, photo3, oriX, oriY,newX,newY
    
    if photo3 == None :
        messagebox.showinfo("ERROR","NO WTERMARK IMAGE")
    else :   
        photo3.resize( int(oriX / 4) , int(oriY / 4) )
        photo2.watermark(photo3,0.5,oriX-newX, oriY-newY)
        displayImage(photo2, oriX, oriY)


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
    photo2=photo ##원본을 띄워주면서 photo2에는 원본들 다시 저장. 처음부터 작업할수있게.

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
    
    degree=askinteger("회전","회전할 각도를 입력하세요",minvalue=-360,maxvalue=360)
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
    photo2.modulate(value,100,100)
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
    

##사진색조절##
def func_inversion():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
    
    value=askinteger("채도","값을 입력하세요(0~100)",minvalue=0,maxvalue=100)
    photo2.modulate(100,100,value)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

##사진스케치###
def func_sketch():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
    
    photo2.charcoal(radius=4.0,sigma=1.0)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

###사진블러처리###
def func_blur():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return

    value=askinteger("Blur","값을 입력하세요(0~10)",minvalue=1,maxvalue=10)
    photo2.blur(sigma=value)
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

###사진엠보싱###
def func_embo():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    
    if photo2 == None:
        return
    
    photo2.transform_colorspace('gray')
    photo2.emboss(radius=2.0, sigma=1.0)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

###사진음영효과###
def func_shadow():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY
    
    if photo2 == None:
        return
    
    photo2.shade(gray=True,azimuth=250.0,elevation=50.0)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

##사진 테두리 자르기
def func_shave():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
    value=askinteger("테두리","자를값을 입력하세요",minvalue=0,maxvalue=100)
    photo2.shave(value,value)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)

####사진에 원 삽입####
def func_circle():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
    
    #draw=Drawing()
    #draw.stroke_color=Color('black')
    #draw.stroke_width=2
    #draw.fill_color=Color('white')
    #draw.ellipse((50,50),(40,20))
    #draw(image)=photo2
    #newX=photo2.width
    #newY=photo2.height
    #displayImage(photo2,newX,newY)    
        
###사진에 삼각형 삽입####
def func_triangle():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return


####사진에 네모 삽입####
def func_squre():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
        
####사진에 글 삽입####
def func_text():
    global window,canvas,paper,photo,photo2,oriX,oriY,newX,newY

    if photo2 == None:
        return
    
    draw = Drawing()
    draw.font_size = 30
    draw.font_color="White"
    value=askstring("TEXT","Only,Eng")
    draw.text(20,50,' '+value+' ')
    draw(photo2)
    newX=photo2.width
    newY=photo2.height
    displayImage(photo2,newX,newY)


###검정펜###
def func_blackpen() :
    global pencolor
    pencolor="black"
    canvas.bind("<B1-Motion>",paint)

###빨간펜###
def func_redpen() :
    global pencolor
    pencolor="red"
    canvas.bind("<B1-Motion>",paint)

###파란펜###
def func_bluepen() :
    global pencolor
    pencolor="blue"
    canvas.bind("<B1-Motion>",paint)

###노란펜###
def func_yellowpen() :
    global pencolor
    pencolor="yellow"
    canvas.bind("<B1-Motion>",paint)

##펜색을 받아 그림을 그리는 함수##
def paint(event):
    global pencolor
    x1,y1=event.x-1,event.y-1
    x2,y2=event.x+1,event.y+1
    canvas.create_oval(x1,y1,x2,y2,fill=pencolor,outline=pencolor)
    
##펜버튼 클릭시 호출되는 클릭펜함수##
def func_clickpen(event):
    value=askinteger("색상","빨강:1 파랑:2 노랑:3 검정:4",minvalue=1,maxvalue=4)
    if value==1:
        func_redpen() ##넘어오는 value에 따라 색상구별
    elif value==2:
        func_bluepen()
    elif value==3:
        func_yellowpen()
    elif value==4:
        func_blackpen()

    
###메인코드부분
window=Tk()
window.geometry("900x600")
window.title("미니 포토샵(Ver_0.2)")

##배경이미지생성
mybg=PhotoImage(file="backgr.png")
bg=Label(window,width=1000,heigh=1000,image=mybg)
bg.place(x=0,y=-200)

##펜버튼생성
mypen=PhotoImage(file="pen.png")
pen=Button(window,image=mypen,cursor="cross")
pen.place(x=825,y=15)
pen.bind("<Button>",func_clickpen)


##제목들어갈 위치##
photo_title=Label(window,text="",fg="white",bg="gray")
photo_title.place(x=10,y=560)

#메뉴생성
##1.메뉴자체생성 및 화면에 디스플레이
##메뉴자체이름=Menu(부모window)
##부모윈도우.config(menu=메뉴자체이름
mainMenu=Menu(window)
window.config(menu=mainMenu)

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
fileMenu.add_command(label="SAVE",command=func_save, state="disable")
fileMenu.add_separator()##구분선 삽입
fileMenu.add_command(label="ORIGINAL",command=func_origin, state="disable")
fileMenu.add_separator()    
fileMenu.add_command(label="WORTERMARK",command=func_watermarkopen ,state="disable")
fileMenu.add_command(label="MARK_IN",command=func_watermark ,state="disable")
fileMenu.add_separator()
fileMenu.add_command(label="CLOSE",command=func_close ,state="disable")
fileMenu.add_command(label="EXIT",command=func_exit)

#추가 상위메뉴생성
imageMenu1=Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="IMAGE_1",menu=imageMenu1 ,state="disable")
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
mainMenu.add_cascade(label="IMAGE_2",menu=imageMenu2 ,state="disable")
#추가2 상위메뉴 속 하위메뉴 생성
imageMenu2.add_command(label="BRIGHT",command=func_bright)
imageMenu2.add_command(label="DARKNESS",command=func_dark)
imageMenu2.add_separator()
imageMenu2.add_command(label="CLEAR",command=func_clear)
imageMenu2.add_command(label="UNCLEAR",command=func_unclear)
imageMenu2.add_separator()
imageMenu2.add_command(label="INVERSION",command=func_inversion)
imageMenu2.add_command(label="SKETCH",command=func_sketch)
imageMenu2.add_command(label="BLUR",command=func_blur)
imageMenu2.add_separator() 
imageMenu2.add_command(label="MONO",command=func_mono)
imageMenu2.add_command(label="EMBOSS",command=func_embo)
imageMenu2.add_command(label="SHADING",command=func_shadow)

#추가3 상위메뉴 생성
imageMenu3=Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="IMAGE_3",menu=imageMenu3 ,state="disable")
#추가3 상위메뉴 속 하위메뉴 생성
imageMenu3.add_command(label="SHAVE",command=func_shave)
imageMenu3.add_separator()
#하위메뉴 속 하위메뉴 생성
DRAW=Menu(imageMenu3,tearoff=0)
imageMenu3.add_cascade(label="DRAW",menu=DRAW)
#하위메뉴 속 하위메뉴 속 메뉴생성
DRAW.add_command(label="●",command=func_circle, state="disable")
DRAW.add_command(label="▲",command=func_triangle, state="disable")
DRAW.add_command(label="■",command=func_squre, state="disable")
DRAW.add_command(label="TEXT",command=func_text)



window.mainloop()
