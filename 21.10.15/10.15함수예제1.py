def plus(v1,v2):         ## 정의하겠다 plus를 (v1,v2)에 대하여 =>함수 선언
    result = 0              ##변수 초기화
    result = v1+v2       ##변수 설정
    return result          ##변수 재 초기화 +>여러번 사용할수 있도록 도와줌.

hap = 0

hap = plus(100,200)
print("100과 200의 plus() 함수의 결과는 %d" %hap)

cap=plus(200,300)
print("200과 300의 plus() 함수의 결과는 %d" %cap)

