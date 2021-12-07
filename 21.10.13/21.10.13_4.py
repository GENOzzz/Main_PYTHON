#while 문#
##while 문으로 2단 출력하기

for i in range(1,10,1):
    print("2x%d=%2d"%(i,2*i))

i=1
while i<10:
    print("2x%d=%2d"%(i,2*i))
    i+=1 #== i=i+1, i++-> 단항연산자

##while 문으로 구구단 출력.##for문을 while 문으로 변경.

for i in range(2,10,1):         
    for k in range(1,10,1):    
        print("%d X %d = %2d" %(i,k,i*k))
    print(" ") 

i=2                 #단 초기화
while i<10:      #단 조건식
    k=1             #곱해지는 수 초기화
    while k<10:  #곱해지는 수 증가식
        print("%dx%d=%2d"%(i,k,i*k))
        k+=1
    i+=1
    print("")

##while문으로 합계구하기
hap = 0 #hap 변수 선언

num1 = int(input("시작값 입력 : ")) #값 입력 받기
num2 = int(input("끝값 입력 : "))
num3 = int(input("증가값 입력 : "))

i = num1 #초기값 while 전에 선언
while i < num2+1: #조건식 (끝값[num2] 보다 작을때 까지)
    hap = hap + i   
    i = i +num3      #증갑식 (while 안에 실행)

print("%d에서 %d 까지 %d씩 증가값의 합 : %d" %(num1,num2,num3,hap))

##for, while문으로 합계구하기
i,hap = 0,0
num =0

num1=int(input("시작값 입력 : "))
num2=int(input("끝값 입력 : "))
num3=int(input("증가값 입력 : "))

for i in range(num1,num2+1,num3): #range(시작값,끝값+1,증가값)
    hap+=i   #hap=hap+i

print("%d에서 %d 까지 %d 씩 증가값의 합 : %d" %(num1,num2,num3,hap))

hap = 0
num1=int(input("시작값 입력 : "))
num2=int(input("끝값 입력 : "))
num3=int(input("증가값 입력 : "))
i=num1
while i < num2+1: #i가 num2+1보다 작을때
    hap=hap+i       #i만큼 더하여라
    i=i+num3        #i에서 num3 만큼 더한 값을.
    print(hap)       #중간에 출력값(hap)을 보여 줘라
print("%d에서 %d까지 %d씩 증가값의 합 : %d"%(num1,num2,num3,hap))

