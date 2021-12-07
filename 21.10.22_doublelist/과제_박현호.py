def ssss(list, x):
        n = len(list)              # 입력 크기 n
        for i in range(n):   # 리스트 a의 모든 값을 차례로
            if x == list[i]:      # x 값과 비교하여            
                return i       # 같으면 위치를 돌려줍니다.



aa=[ ]                                                                                                            ##빈 리스트 aa생성
while True:                                                                                                    ##while문으로 시작
    b=input("리스트를 작성 하시겠습니까? : (yes=y,no=n)")                   ##b에 리스트 작성여부를 입력받음
    if str (b)=='y':                                                                                             ##b가 y라면 아래 실행
        x=int(input("몇개로 구성된 리스트를 작성 하시겠습니까? : "))     ##리스트의 요소 갯수를 입력받음
        for i in range(x):                                                                                    ##입력 받은값 (x)만큼 
            aa.append(int(input(str(i)+"번째 숫자를 입력해 주십시오 : ")))  ##aa라는 리스트에 임의의 숫자들을 입력받음
            
        print(aa)                                                                                                 ##aa리스트 출력

        a= int(input("탐색할 값을 입력하십시오 : "))                                     ##a에 탐색할 임의의 값을 입력받음
        if  not a in aa:                                                                                         ##만약 값a가 리스트 aa안에 없으면
            print("없어요.")                                                                                   ##없어요 출력
        else:                                                                                                         ##그렇지 않다면(==ar가 aa리스트 안에 있으면)
            ssss(aa,a)                                                                                           ##ssss함수 실행
            print("%d의 위치는 [%d]번째 입니다."%(a,ssss(aa,a)))               ##a의 위치는 i번째 입니다.

        aa=[]                                                                                                         ##aa리스트 비워주기 (반복문이라 리스트가 쌓임)
    elif str (b)=='n':                                                                                              ##while문 안에서 b가 n일경우
        print("프로그램을 종료합니다.")                                                            ##프로그램 종료 출력
        break                                                                                                         ##while문 break
