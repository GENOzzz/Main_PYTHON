a=0

def coffee(button):
    print()             #결과값에 공백출력
    print("#1물")
    print("#2종이컵")

    if button ==1:      #1입력시 보통출력
        print("#3보통")
    elif button == 2:  #2입력시 설탕 출력
        print("#3설탕")
    elif button == 3:  #3입력시 블랙출력
        print("#블랙")
    else :                 #4그외 아무거나 출력
        print("#3.아무거나\n")

    print("#4물")
    print("#5녹임")
    print()

a=int(input("어떤커피? (1,2,3)"))   #변수 받기
coffee(a)                                      #함수 coffee에 a 적용
print("여기요")                              #마지막 안내 멘트
