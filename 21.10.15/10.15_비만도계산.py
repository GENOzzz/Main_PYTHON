##21.10.15_박현호##

while True:
    try:
        s=int(input("성별을 입력하세요 (남성1,여성2) : "))

        if s<1 or 2<s:
            print("1또는 2만 입력해 주십시오")
            continue

        k=int(input("체중을 입력하세요 : "))

        if s==1 and k>=85 :
            print("과체중입니다. 운동하세요.")
        elif s==1 and 50<=k<85:
            print("표준체중입니다. 현 페이스 유지하세요.")
        elif s==1 and k<50:
            print("표준체중 이하입니다. 고기먹고 운동하세요.")
      
        if s==2 and k>=68 :
            print("과체중입니다. 운동하세요.")
        elif s==2 and 40<=k<68:
            print("표준체중입니다. 현 페이스 유지하세요.")
        elif s==2 and k<40:
            print("표준체중 이하입니다. 고기먹고 운동하세요.")
            
    except ValueError :                                   
        print("숫자만 입력해 주십시오")       
