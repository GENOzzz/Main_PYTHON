#if ~ elif ~ else문
score=int(input("점수를 입력하세요 : "))

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
