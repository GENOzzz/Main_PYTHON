#20211006파이썬 계산기_박현호#
#변수 선언#
a=int(input("첫번째 숫자를 입력하세요 : ")) #input()함수는 사용자로부터 임의의 값을 입력받은 후 변수 a에 대입(=)
b=int(input("두번째 숫자를 입력하세요 : "))#input()함수는 사용자로부터 임의의 값을 입력받은 후 변수 b에 대입(=)
#산술연산자를 통한 사칙연산#
result=a+b
print(a,"+",b,"=",result)
result=a-b
print(a,"-",b,"=",result)
result=a*b
print(a,"*",b,"=",result)
result=a/b
print(a,"/",b,"=",result)
