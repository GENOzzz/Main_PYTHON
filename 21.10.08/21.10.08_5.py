##변수 선언 - 계산기 ##

a, b, ch = 0, 0, ""

#메인 코드 부분#
a=int(input("첫 번째 수를 입력하세요 : "))
ch = input("계산할 연산자를 입려하세요 : ")
b=int(input("두 번째 수를 입력하세요 : "))

if ch=="+" :
    print("%d + %d = %d 입니다." %(a, b, a+b))
elif ch=="-" :
    print("%d - %d = %d 입니다." %(a, b, a-b))
elif ch=="*" :
    print("%d * %d = %d 입니다." %(a, b, a*b))
elif ch=="/" :
    print("%d / %d = %d 입니다." %(a, b, a/b))
elif ch=="%" :
    print("%d %% %d = %d 입니다." %(a, b, a%b)) #나머지 값.
elif ch=="//" :
    print("%d // %d = %d 입니다." %(a, b, a//b)) #나누기 몫
elif ch=="**" :
    print("%d ** %d = %d 입니다." %(a, b, a**b)) #제곱
else :
    print("알수없는 연산입니다.")
