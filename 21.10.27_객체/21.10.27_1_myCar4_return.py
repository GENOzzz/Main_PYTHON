class Car :                               

    name=""                                 
    speed=0                                 


    def __init__(self,name,value):
        self.name=name
        self.speed=value

    def getName(self):        
        return self.name             

    def getSpeed(self):     
        return self.speed                  

Car1, Car2, Car3 = None, None, None       

Car1=Car("벤츠",30)                                

Car2=Car("아우디",60)

Car3=Car("벤틀리",80)



        
print("%s 의 현재속도는 %d km 입니다."%(Car1.getName(),Car1.getSpeed()))

     
print("%s 의 현재속도는 %d km 입니다."%(Car2.getName(),Car2.getSpeed()))

       
print("%s 의 현재속도는 %d km 입니다."%(Car3.getName(),Car3.getSpeed()))

