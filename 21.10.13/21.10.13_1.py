##for~반복문##

for i in range(0,3,1) :
                #range(시작값,끝값+1,증가값) => 시작값 ~ 끝값까지 증가값만큼 증가
    print("안녕하세요? for문을 공부중입니다. ^^")
    
for i in range(1,5,1) :
    print("안녕하세요? for문을 공부중입니다. ^^",i)

for i in range(1,5,1) :
    print("%d : 안녕하세요? for 문을 공부중입니다^^" %i) #%d 자리에 i를 출력.

##배열##
for i in range(0,3,1) :
    print("안녕하세요? for문을 공부중입니다. ^^")
#range함수를 배열로 바꿀수 있음.
for i in [0,1,2] :
    print("안녕하세요? for문을 공부중입니다. ^^")
##1~5까지 차례로 출력
for i in range(1,6,1):
    print("%d"%i,end="  ")##end=" "-> 줄바꿈 없이" "공백 만큼 띄워서 다음 결과 출력

print("\n")#줄바꿈

for i in range(6): #=range(0,6,1)
    print("%d"%i,end="  ")

print("\n")

##1부터 10까지의 합을 구하기

i,hap=0,0 # 변수 hap 선언하고 시작할것

for i in range(1,11,1):
    hap=hap+i #hap + = i 와 같음
print("1에서 10까지의 합 : %d 입니다"%hap)

print("\n")

#1부터 10까지의 곱
hap=1
for i in range(1,11,1):
    hap=hap*i
    print(hap) #중간에 hap 의 결과값 출력.
print("1에서 10까지의 곱 : %d 입니다"%hap)

