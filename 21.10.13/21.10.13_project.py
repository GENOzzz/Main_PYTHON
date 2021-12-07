##학점산출 무한루프 - 0~100 까지만 입력 받을 수 있도록.
'''
while True :
    score=int(input("점수를 입력하세요 : "))
    if score >=90 and score <=100 :
        print("A")
    elif score >=80 and score <90:
        print("B")
    elif score >=70 and score <80:
        print("C")
    elif score >=60 and score <70:
        print("D")
    elif score >=0 and score <60:
        print("F")
    else :                                          #else - if에서 걸어준 조건 외(0~100 외)
        print("잘못 된 점수 입니다.")
    print("학점입니다")
'''
## try문 예시##
while True :
    try:                                                            #try: => 일단 실행해라 아래 코드를.
        score=int(input("점수를 입력하세요 : "))
        if score >=90 and score <=100 :
            print("A")
        elif score >=80 and score <90:
            print("B")
        elif score >=70 and score <80:
            print("C")
        elif score >=60 and score <70:
            print("D")
        elif score >=0 and score <60:
            print("F")
        else :
            print("잘못 된 점수 입니다.")
        print("학점입니다")
    except ValueError :                                   #except ValueError : 만약 예외가 생긴다면 ~
        print("점수를 입력해 주십시오")
