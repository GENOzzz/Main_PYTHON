from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from wand.image import *

# 함수 정의 부분
def displayImage(img, width, height) :
    global window,canvas, paper, photo, photo2, oriX, oriY

    window.geometry(str(width)+"x"+str(height))
    if canvas != None :
        canvas.destroy()

    canvas = Canvas(window, width=width, height=height)
    paper=PhotoImage(width=width, height=height)
    canvas.create_image( (width/2, height/2), image=paper, state="normal")

    blob = img.make_blob(format='RGB')
    for i in range(0, width) :
        for k in range(0, height) :
            r = blob[(i*3*width)+(k*3) + 0]
            g = blob[(i*3*width)+(k*3) + 1]
            b = blob[(i*3*width)+(k*3) + 2]
            paper.put("#%02x%02x%02x" % (r,g,b) , (k, i))

    canvas.pack()

def func_open() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    readFp = askopenfilename(parent=window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),  ("모든 파일", "*.*") ))
    photo = Image(filename=readFp)
    oriX = photo.width
    oriY = photo.height

    photo2 = photo.clone()
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_save() :
    global window,canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None :
        return
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", filetypes=(("JPG 파일", "*.jpg;*.jpeg"),  ("모든 파일", "*.*") ))
    savePhoto = photo2.convert("jpg")
    savePhoto.save(filename=saveFp.name)

def func_exit() :
    window.quit()
    window.destroy()

def func_zoomin() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대배수", "확대할 배수를 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.clone()
    photo2.resize( int(oriX * scale) , int(oriY * scale) )
    newX = photo2.width 
    newY = photo2.height    
    displayImage(photo2, newX, newY)

def func_zoomout() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("축소", "축소할 배수를 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.clone()
    photo2.resize( int(oriX / scale) , int(oriY / scale) )
    newX = photo2.width 
    newY = photo2.height    
    displayImage(photo2, newX, newY)

def func_mirror1() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.flip()
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_mirror2() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.flop()
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_rotate() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    degree = askinteger("회전", "회전할 각도를 입력하세요", minvalue=0, maxvalue=360)
    photo2 = photo.clone()
    photo2.rotate(degree)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_bright() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("밝게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)
    photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)    

def func_dark() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("어둡게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)
    photo2 = photo.clone()
    photo2.modulate(value, 100, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)
    
def func_clear() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("선명하게", "값을 입력하세요(100~200)", minvalue=100, maxvalue=200)
    photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_unclear() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    value = askinteger("탁하게", "값을 입력하세요(0~100)", minvalue=0, maxvalue=100)
    photo2 = photo.clone()
    photo2.modulate(100, value, 100)
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)
    
def func_bw() :
    global window,canvas, paper, photo, photo2, oriX, oriY
    photo2 = photo.clone()
    photo2.type="grayscale"
    newX = photo2.width 
    newY = photo2.height
    displayImage(photo2, newX, newY)
    
# 변수 선언 부분
window,canvas, paper=None, None, None
photo, photo2=None, None
oriX,oriY= 0,0

# 메인 코드 부분
window = Tk()
window.geometry("250x250")
window.title("미니 포토샵(Ver 0.1)")

mainMenu = Menu(window)
window.config(menu=mainMenu)
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack( expand=1, anchor=CENTER)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_command(label="파일 저장", command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(1)", menu=image1Menu)
image1Menu.add_command(label="확대", command=func_zoomin)
image1Menu.add_command(label="축소", command=func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label="상하 반전", command=func_mirror1)
image1Menu.add_command(label="좌우 반전", command=func_mirror2)
image1Menu.add_command(label="회전", command=func_rotate)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label="이미지 처리(2)", menu=image2Menu)
image2Menu.add_command(label="밝게", command=func_bright)
image2Menu.add_command(label="어둡게", command=func_dark)
image2Menu.add_separator()
image2Menu.add_command(label="선명하게", command=func_clear)
image2Menu.add_command(label="탁하게", command=func_unclear)
image2Menu.add_separator()
image2Menu.add_command(label="흑백이미지", command=func_bw)
window.mainloop()
