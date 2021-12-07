##21.10.15_박현호##

while True :
    try:                                                            
        score=int(input("점수를 입력하세요 : "))
        print("축하")
        if score >=95 and score <=100 :
            print("\b""축하드립니다. A+ 학점입니다.")
        elif score >=90 and score <95:
            print("축하드립니다. A 학점입니다.")
        elif score >=85 and score <90:
            print("축하드립니다. B+ 학점입니다.")
        elif score >=80 and score <85:
            print("축하드립니다. B 학점입니다.")
        elif score >=75 and score <80:
            print("축하드립니다. C+ 학점입니다.")
        elif score >=70 and score <75:
            print("축하드립니다. C 학점입니다.")
        elif score >=65 and score <70:
            print("축하드립니다. D+ 학점입니다.")
        elif score >=60 and score <65:
            print("축하드립니다. D 학점입니다.")
        elif score >=0 and score <60:
            print("축하는 못드립니다. F 학점입니다.")
        else :
            print("잘못된 점수입니다. 바르게 입력해주십시오.")
    except ValueError :                                
        print("점수를 입력해 주십시오")
