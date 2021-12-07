def calc(v1, v2, op) :              ##calc 함수 선언
    result : 0                              
    if op == '+'  :                        ##op 를 연산자로 받겠다
        result = v1 + v2               ##해당 연산자에 따라 result를 v1,v2를 계산 하겠다.
    elif op == '-' :
        result= v1 - v2
    elif op == '*' :
        result= v1 * v2
    elif op == '/' :
        result= v1 / v2

    return result

res=0
var1,var2,oper=0,0,""
while True :
    var1=int(input("첫 번째 숫자 입력 : "))
    oper=input("연산자 입력 (+, -, *, /) : ")
    var2=int(input("두 번째 숫자 입력 : "))

    res=calc(var1,var2,oper)

    print("##계산기 : %d%s%d=%d" %(var1,oper,var2,res))
