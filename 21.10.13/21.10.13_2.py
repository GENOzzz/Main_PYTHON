##500에서 1000사이에 있는 홀수의 합을 구하여보자##
i,hap=0,0

for i in range(501,1001,2):
    hap+=i # == hap = hap+i

print("500에서 1000까지 홀수의 합 : %d" %hap)
print("\n")

#if문과 결합#
for i in range(500,1001,1):
    if i %2 != 0: #==비교연산자 사용 하여 참 거짓 판별 ,## != 0 -> 0이 아닐때(홀수)
        hap+=i     #if 문 안에 들어갈 수 있도록 들여쓰기
print("500에서 1000까지 홀수의 합 : %d" %hap)

##입력한 값까지 for문으로 합계 구하기##
i,hap = 0, 0 #hap = 0, 만 작성해도 결과도출가능.
num = 0

num = int(input("값 입력 : ")) #끝값을 사용자로부터 받음
                                            # ↓
for i in range(1, num+1, 1) : #끝값을 변수로 지정가능
    hap+=i

print("1에서 %d 까지 합 : %d" %(num,hap))

##응용##
i,hap = 0, 0
num = 0

num1 = int(input("시작값 입력 : "))
num2 = int(input("끝값 입력 : "))
for i in range(num1, num2+1, 1) :   
    hap+=i

print("%d에서 %d 까지 합 : %d" %(num1,num2,hap))

i,hap = 0, 0
num = 0

num1 = int(input("시작값 입력 : "))
num2 = int(input("끝값 입력 : "))
num3 = int(input("증가값 입력 : "))
for i in range(num1, num2+1, num3) :   
    hap+=i

print("%d에서 %d 까지 %d씩 증가값의 합 : %d" %(num1,num2,num3,hap))
