###클래스 정의
class Car :                                 ##클래스 car는
 ##필드부분
    color=""                                  ##필드 color 선언 및 초기값
    speed=0                                 ##필드 speed 선언 및초기값 대입

##메소드 부분
    def upSpeed(self,value):        ##메소드 upSpeed는 (A,x) 정의.
        self.speed+=value              ##A.speed에 x값을 더한다.

    def downSpeed(self,value):     ##함수 upSpeed는 (A,x) 정의.
        self.speed-=value                   ##A.speed에 x값을 뺀다.
###생성자
        ##생성자는 인스턴스 생성시  무조건 자동실행. Car1.py와 비교 해볼것
    def __init__(self):                     
        self.color="빨강"
        self.speed=0
        
##메인 코드부분
myCar1=Car()                                ##myCar1 인스턴스생성

myCar2=Car()

myCar3=Car()



myCar1.upSpeed(30)          ##Car1실행부
print("자동차 1의 색상은 %s 이며 , 현재속도는 %d km 입니다."%(myCar1.color,myCar1.speed))

myCar2.upSpeed(60)          ##Car2 실행부
print("자동차 2의 색상은 %s 이며 , 현재속도는 %d km 입니다."%(myCar2.color,myCar2.speed))

myCar3.upSpeed(0)            ##Car3 실행부
print("자동차 3의 색상은 %s 이며 , 현재속도는 %d km 입니다."%(myCar3.color,myCar3.speed))


