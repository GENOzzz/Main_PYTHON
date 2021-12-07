class Car:                                                  ##부모 클래스(Car)
        speed = 0

        def upSpeed(self, value):
            self.speed+=value

        def downSpeed(self, value):
            self.speed-=value

class Sedan(Car):                                   ##부모클래스(Car)를 받은 자식클래스 (Sedan)
    seatNum=0

    def getSeatNum(self):
        return self.seatNum

class Truck(Car):                                    ##부모클래스(Car)를 받은 자식클래스(Truck)
    capacity = 0

    def getCapacity(self):
        return self.capacity

sedan1,truck1=None, None

sedan1=Sedan()
truck1=Truck()

sedan1.upSpeed(100)
truck1.upSpeed(80)

sedan1.seatNum=5
truck1.capacity=50

print("세단의 속도는 %d 좌석수는 %d개 입니다"%(sedan1.speed,sedan1.getSeatNum()))
print("트럭의 속도는 %d 총중량은 %d톤입니다."%(truck1.speed,truck1.getCapacity()))
