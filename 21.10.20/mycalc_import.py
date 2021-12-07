from mycalc import *

in1=float(input("첫번째 숫자를 입력하세요 : "))
op=input("연산자(+, -, *, /)를 입력하세요 : ")
in2=float(input("두번째 숫자를 입력하세요 : "))

print()
print("^^^모듈로 작성한 계산기 호출 결과^^^")
if op == '+' :
    print("%5.1f+%5.1f=%5.1f "%(in1, in2, plus(in1, in2)))
elif op == '-' :
    print("%5.1f-%5.1f=%5.1f "%(in1, in2, minus(in1, in2)))
elif op == '*' :
    print("%5.1f*%5.1f=%5.1f "%(in1, in2, multiply(in1, in2)))
elif op == '/' :
    print("%5.1f-%5.1f=%5.1f "%(in1, in2, divide(in1, in2)))
else :
    print("연산자를 모르겠습니다.")
