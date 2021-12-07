
def func1() :     ##func1 선언
    #global a        ##a를 전역변수로 선언.
    a=10            ##지역변수 =>func1 에서는 선언된  a가 우선됨.
    print("func1()에서 a의 값 % d" %a)##쓰고 버려짐

def func2() :
    print("func2()에서 a의 값 %d" %a)


a=20                ##전역변수

func1()         ##func1에서 a를 global로 전역변수로 선언하게 되면 a는 func2에도 10으로 들어감
#a=20  => 다시 전역변수 선언 하면 func1에서 선언한 a의 값이 20으로 바뀜
func2()

result=0
def func1() :
    global result
    result = 100
    return result

def func2():
    return print("반환값이 없는 함수 실행")

hap = 0

hap=func1() #return 값을 hap에 대입
print("func1()에서 돌려준값 == %d" %hap)
func2() #return값이 없어 에러 출력
