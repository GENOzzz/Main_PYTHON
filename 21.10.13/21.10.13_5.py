##무한루프
'''
while True : #항상 참이다.
    print("♥", end=" ") #∴♥중지 시키기 전까지 출력

##무한루프 합계구하기
while True : #무한루프를 적용하려면 while 조건식 : 의 조건식을 True로 지정
    hap = 0                                             #한번에 들여쓰기는 드래그 후 tap키
    num1=int(input("시작값 입력 : "))
    num2=int(input("끝값 입력 : "))
    num3=int(input("증가값 입력 : "))
    i=num1
    while i < num2+1:
        hap=hap+i
        i=i+num3        
    print("%d에서 %d까지 %d씩 증가값의 합 : %d"%(num1,num2,num3,hap))
#무한루프  중지 Ctrl + c 키

'''
##입력한 두 수의 합계를 반복해서 계산하는 프로그램
hap = 0
a,b=0,0

while True :
    a=int(input("첫 번째 수 입력 : "))
    b=int(input("두 번째 수 입력 : "))
    hap=a+b
    print("%d+%d=%d"%(a,b,hap))


##분기문 1, 반목문을 탈출하는 break 문

for i in range(1,100):
    print("for문을 %d번 실행했습니다." %i)
    break

##입력한 두 수의 합계를 반복해서 계산하는 프로그램 break
hap = 0
a,b=0,0

while True :
    a=int(input("첫 번째 수 입력 : "))
    if a == 0 :
        break
    b=int(input("두 번째 수 입력 : "))
    if b == 0 :
        break
    hap=a+b
    print("%d+%d=%d"%(a,b,hap))

print("0을 입력해서 반복문을 탈출했습니다.")


##분기문 2, 반복문으로 돌아가는 continue 문
hap = 0
a,b=0,0

while True :
    a=int(input("첫 번째 수 입력 : "))
    if a == 0 :
        continue    #continue를 만나면 남은 블록 건너뛰고 반복문 처음으로 되돌아감
    b=int(input("두 번째 수 입력 : "))
    if b == 0 :
        continue
    hap=a+b
    print("%d+%d=%d"%(a,b,hap))
  
##1~100까지 더하되 3의 배수를 제외하고 더하는법
hap,i=0,0

for i in range(1,101):
    if i %3 ==0 : #3으로 나눈 나머지가 0일 때(3의 배수일 때)
        continue  #남은 부분을 건너뛰고 처음으로 돌아가라
    
    hap+=i        #나머지가 0이 아닐 경우 더하여라
    print(i,hap)  #현재 i값과 hap값 출력.
print("1~100의 합계(3의 배수 제외) : %d" %hap) #더한값 출력

a,b=0,0

for b in range(1,101):
    if b %3 ==0 :
        continue
    
    a +=b
    
print("1~100의 합계(3의 배수 제외) : %d" %a)

##1~100까지 합에서 1000이 넘을때 위치
hap,i=0,0

for i in range(1,101) : #1~100까지 진행
    hap += i                #더하면서 진행

    if hap>=1000:       #합이 1000과 같거나 클경우
        break               #멈춰라
    print(i,hap)            #계산과정을 보여달라
print("1~100의 합에서 최초로 1000이 넘는 위치 : %d" %i)

a,b=0,0

for b in range(1,101) :
    a += b

    if a>=1000:
        break
    print(b,a)
print("1~100의 합에서 최초로 1000이 넘는 위치 : %d" %b)

##for ~ if 문 응용##
##홀수제외 더하기
a,b=0,0

for b in range(1,101):
    if b %2 != 0 : #2로나눈 나머지가 0이 아닐때(홀수일때)
        continue   #남은 블럭은 건너뛰고 처음으로 돌아가라
    
    a +=b
    print(b,a)
print("1~100의 합계(홀수제외) : %d" %a)
##짝수제외 더하기
a,b=0,0

for b in range(1,101):
    if b %2 == 0 :  #2로나눈 나머지가 0일 때(짝수일때)
        continue     #남은 블럭은 건너뛰고 처음으로 돌아가라
    
    a +=b
    print(b,a)
print("1~100의 합계(짝수제외) : %d" %a)

