##2단 출력##
for i in range(1,10,1):
    print("2 x %d = %d"%(i,2*i))
##3단 출력##
for i in range(1,10,1):
    print("3 x %d = %d"%(i,3*i))
##4단 출력##
for i in range(1,10,1):
    print("4x%d = %d"%(i,4*i))

##구구단출력##
i,a=0,0

a=int(input("몇단 ? "))

for i in range(1,10,1) :
    print("%d x %d =%2d" %(a,i,a*i)) #%2d = 끝자리 수부터 자리를 맞추기 위함.

print("\n")

##중첩for문으로 구구단 출력##
for i in range(2,10,1):         #i는 2~9까지 증가한다. 단 k증가 조건 생성
    for k in range(1,10,1):    #i가 1일때 k는 1~9까지 증가한다.
                                        #k가 9를 넘어가면 i가 1증가한다
                                        #i가 9가 될때까지 반복한다.
                                        #i가 9일때 k가 9일때 종료.
        print("%d X %d = %2d" %(i,k,i*k)) #%2d = 숫자의 자리를 맞추기위함
    print(" ") # 한단이 끝나고 자리 띄우기.


