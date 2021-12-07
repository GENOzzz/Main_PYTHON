
def para_func(*para) : ##가변 매개변수 =>변수 몇개가 들어올지 모른다.
    print(para)
    print(type(para))  ##class : tuple => (a,b,c) ->읽기만하고 수정불가능 [a,b,c] 와 다름.
    result = 0                                          ##주민번호 등 수정되면 안되는 자료에 활용
    for num in para :
        result =result + num

    return result

hap = 0

hap=para_func(11,22)
print("매개변수 2개 함수 호출결과 : %d" %hap)
hap=para_func(11,22,33)
print("매개변수 3개 함수 호출결과 : %d" %hap)


def dic_func(**para) : ##(**para) => 가변매개변수 - 딕셔너리형식.
    print(para)               ##딕셔너리 전체 출력 {'아이오아이': 11, '소녀시대': 8, '걸스데이': 4, 'AOA': 7}
    print(type(para))     ##para의 타입 출력 <class 'dict'> : 각 리스트에 이름을 붙여 필요한 자료만 찾을 수 있음.
    print(para.keys())   ##para의key 만 출력
    for k in para.keys():
        print("%s : %d 명입니다." %(k,para[k]))

dic_func(아이오아이 = 11, 소녀시대 = 8, 걸스데이 = 4, AOA =7)
             ##(key = 값 , key = 값 , key = 값 , key = 값  )


def dic_func(*para) : 
    print(para)              
    print(type(para))    
    for num in para:
        print("%d 명입니다." %num)

dic_func( 11,  8,  4, 7)


def dic(a):
    for i in range(0,a[5],1): #해당 배열의 5번째에 있는 무언가를 가져와 for에 넣ㅇ...
        if i<0:
            continue
        else :
            print("{}의{}번째는{}".format(a,i,a[i]))

c=[0,1,2,3,4,6]
print(c[5])
dic(c)
