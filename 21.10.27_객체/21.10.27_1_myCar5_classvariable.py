class Car :                               

    name=""                                 
    speed=0
    count=0


    def __init__(self,name,value):
        self.name=name          ##인스턴스 변수
        self.speed=value          ##인스턴스 변수
        Car.count+=1               ##클래스 변수 => 인스턴스명이냐 클래스 명이냐에 따라 정해짐.

Car1, Car2, Car3 = None, None, None       

Car1=Car("벤츠",30)
print("%s의 현재속도는 %d, 생산된 자동차는 총 %d대 입니다."%(Car1.name,Car1.speed,Car.count))

Car2=Car("아우디",60)
print("%s의 현재속도는 %d, 생산된 자동차는 총 %d대 입니다."%(Car2.name,Car2.speed,Car.count))

Car3=Car("벤틀리",80)
print("%s의 현재속도는 %d, 생산된 자동차는 총 %d대 입니다."%(Car3.name,Car3.speed,Car.count))

print(Car.count)

class Carr:
    name=""
    speed=0

    def __init__(vivi):
        vivi.name="마이바흐"
        vivi.speed=0

Car11=Carr()
print("%s,%d"%(Car11.name,Car11.speed))

