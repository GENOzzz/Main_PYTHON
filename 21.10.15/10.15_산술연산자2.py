##21.10.15_박현호##
while True:
    a,b,c,d,e = 0,0,0,0,0
    
    m=int(input("다섯자리 정수를 입력해 주세요 : "))
    if m<0 or m>99999:
        print("숫자를 재입력해 주세요")
        continue
    
    print("%d"%(m))

    a=m//10000
    b=m%10000//1000
    c=m%1000//100
    d=m%100//10
    e=m%10//1

    print("%d+%d+%d+%d+%d=%d"%(a,b,c,d,e,a+b+c+d+e))    
