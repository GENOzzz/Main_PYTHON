##함수 정의 부분##
def plus(v1,v2) :           ##def ->함수 정의, plus라는 함수는 v1,v2를 넣었을때
    result = 0                #변수 선언
    result = v1 + v2        #v1+v2를 실행한다
    return result             #return -> 값을 토해낸다.

##변수 선언 부분
hap=0

##메인 코드 부분
hap = plus(100,200)
print("100과 200의 plus()함수 결과는 %d 입니다." %hap)
