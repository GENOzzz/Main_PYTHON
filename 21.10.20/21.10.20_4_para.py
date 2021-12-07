
def para2_func(v1,v2) :
    result = 0
    result = v1+v2
    return result

def para3_func(v1,v2,v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0

hap=para2_func(10,20,30) 
print("매개변수 2개 함수 호출 결과 : %d" %hap)

hap=para3_func(10,20,30)    
print(" 매개변수 3개 함수 호출 결과 : %d" %hap)


##매개변수가 부족하거나 많은경우 에러가 발생하게 됨.
##Error: para2_func() missing 1 required positional argument: 'v2'
##Error: para2_func() takes 2 positional arguments but 3 were given

def para_func(v1,v2,v3=1) : ##매개변수 자체에 초기값 설정 가능
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0

hap=para_func(10,20)   ##v3 에 대한 초기값이 설정되어 있으므로 입력하지 않아도 출력 가능
print("매개변수 2개 함수 호출 결과 : %d" %hap)

hap=para_func(10,20,30)  ##v3를 선언할 경우 초기값을 덮고 입력한 값으로 출력이됨
print(" 매개변수 3개 함수 호출 결과 : %d" %hap)
