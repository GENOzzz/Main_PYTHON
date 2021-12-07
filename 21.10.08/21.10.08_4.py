##if문 안에 if문##
a=int(input("정수를입력하세요"))
if a>50 :
    if a <100:
        print("50보다크고 100보다 작군요")
    else :
        print("올 ㅋ 100 보다 크거나 같군여")
else :
    print("에게 50보다 작네 ㅋ ")


##중첩 if문의 사례## ##학점 계산기##
a=int(input("점수를입력하세요"))
if a >=90 :
    print("A", end=" ")
else :
    if a >= 80 :
        print("B", end=" ")
    else :
        if a >= 70 :
            print("C", end=" ")
        else :
            if a >= 60 :
                print("D", end=" ")
            else :
                print("F 낙제", end=" ")
print("학점입니다.")

#if ~elif ~else 문#
a=int(input("점수를입력하세요")) #elif == else+if 를 줄여서 쓸수 있음.
if a >=90 :
    print("A", end=" ")
elif a >= 80 :
    print("B", end=" ")
elif a >= 70 :
    print("C", end=" ")
elif a >= 60 :
    print("D", end=" ")
else :
    print("F 낙제", end=" ")
print("학점입니다.")
