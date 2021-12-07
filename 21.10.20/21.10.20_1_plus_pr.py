
def plus(v1,v2) :           ##def  함수명(매개변수 1, 매개변수 2...)
    result = 0               ##변수선언,초기화
    result = v1 + v2
    return result            ##반환값 -> print까지 함수 에 포합시킬수있음.=> return이 필요없음.
## print("%d과(와) %d의 plus()함수 결과는 %d 입니다." %(v1,v2,hap))

while True :
    hap=0


    a=int(input("첫번째 숫자를 입력해 주십시오 : "))
    b=int(input("두번째 숫자를 입력해 주십시오 : "))

    hap = plus(a,b)
    print("%d과(와) %d의 plus()함수 결과는 %d 입니다." %(a,b,hap))
