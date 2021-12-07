'''
##리스트 활용전
a,b,c,d=0,0,0,0
hap=0

a=int(input("1번째 숫자 입력 : "))
b=int(input("2번째 숫자 입력 : "))
c=int(input("3번째 숫자 입력 : "))
d=int(input("4번째 숫자 입력 : "))

hap=a+b+c+d

print("합계 : %d" %hap)
'''
'''
##리스트 활용
aa=[0,0,0,0]
hap=0

aa[0]=int(input("1번째 숫자 입력 : "))
aa[1]=int(input("2번째 숫자 입력 : "))
aa[2]=int(input("3번째 숫자 입력 : "))
aa[3]=int(input("4번째 숫자 입력 : "))

hap=aa[0]+aa[1]+aa[2]+aa[3]

print("합계 : %d " %hap)
'''
'''
##빈 리스트와 append를 이용한 리스트의 추가
aa=[]                   ##빈리스트 생성
aa.append(0)    ##append(값) 함수로 리스트에 하나씩 추가.
aa.append(0)
aa.append(0)
aa.append(0)
aa.append(0)
print(aa)               ##결과값 : [0,0,0,0,0] 의 리스트 생성
'''
'''
##for문을 이용한 append 사용
aa=[]
for i in range(1000):
    aa.append(0)

print(aa)
'''
'''
##for문을 이용한 리스트 생성 및 입력값에 따라 합계출력
aa=[]
for i in range(4):      ##range(4) == range(0,4,1)
    aa.append(0)
hap = 0

for i  in range(4):
    aa[i]=int(input(str(i+1) + "번째 숫자 : "))

hap=aa[0]+aa[1]+aa[2]+aa[3]

print("합계 : %d" %hap)
'''
##리스트와 for문을 이용한 최종 진화형태
aa=[]
hap=0
for i in range(4):      ##range(4) == range(0,4,1)
    aa.append(0)                                                                                
    aa[i]=int(input(str(i+1) + "번째 숫자를 입력해 주세요 : "))
    hap = hap+aa[i]       ##for i in range(4)반복 되니까 합쳐줄수있음
print(aa)
print(hap)



