while True:
    try :
        score=int(input("점수를 입력하세요 : "))

        if score<0 or score>100:
            continue

        if score >= 90 :
            print("A", end="")
        elif score >= 80 :
            print("B", end="")
        elif score >= 70 :
            print("C", end="")
        elif score >= 60 :
            print("D", end="")
        else :
            print("F", end="")

        print("학점 입니다. ^^")
    except ValueError:
        print("정수를 입력해주세요.")
        continue
