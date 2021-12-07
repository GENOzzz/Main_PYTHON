##튜플 : 한번 만들고 나면 변경할 수 없는 집합
##리스트는 [ ] , 튜플은 ( ), 딕셔너리는 { } 로 생성
            #   대괄호         소괄호               중괄호
##튜플은 값을 수정할 수 없으며 읽기만 가능하므로 읽기 전용의 자료를 저장할 때 사용

mytuple=(1,2,3)
print(type(mytuple))    ## type => 데이터 형식 출력
print(mytuple)              ##mytuple 출력
print(mytuple[0])          ##튜플과 리스트의 공통점 : 인덱스로 값을 불러올 수 있다.
print(mytuple[1])
print(mytuple[2]) 

'''
mytuple[1] = 20            ##TypeError: 'tuple' object does not support item assignment
                                      ##튜플은 값을 변경할 수 없음.
'''
'''
mytuple1,mytuple2,mytuple3=1,2,3 ##여러 변수에 수를 순차적으로 대입 => 변수로 인식

print(mytuple1)
print(mytuple2)
print(mytuple3)

mytuple1=1,2,3          ##하나의 변수명에 여러개의 수를 넣을경우 (소괄호 없이) 튜플로 인식
print(type(mytuple1))
print(mytuple1)

mytuple=[1]                 ##리스트에 하나의 값은 넣어줄수 있음.
print(mytuple)

mytuple2=(1)               ##소괄호 안에 숫자가 하나만 들어갈 경우
print(type(mytuple2))  ##<class 'int'> => 정수형으로 인식
print(mytuple2)

mytuple3=(1,)               ##소괄호 안에 숫자가 하나만 들어갈 경우 콤마(,)를 넣어주어야
print(type(mytuple3))  ##<class 'tuple'> => 튜플로 인식
print(mytuple3)
'''
##딕셔너리 : 인덱스가 아닌 키로 값을 지정.
##리스트의 인덱스 대신 키 사용, 딕셔너리는 키를 이용하여 값을 찾아낼때 편리
##딕셔너리는 리스트와 달리 값의 순서를 지켜주지 않는다 => 키로 위치를 찾으므로 순서 불필요

#학생 정보의 리스트 표현

student1=[20,'홍길동','빅데이터']

#학생 정보의 딕셔너리 표현
student2={'학번' : 20,'이름' : '고길동','전공' : '빅데이터'} 
            ##   ' 키 ' : 값
##print(student2[0])          ##KeyError: 0 => 인덱스로 호출시 에러발생

student3={0 : 20,'이름' : '홍길동','전공' : '알고리즘'} 
            ##   ' 키 ' : 값
print(student3[0],student3['이름'],student2['이름'])

##딕셔너리에 값 추가

student2['연락처']='010-1234-1234' #해당 키에 값이 없는 경우 키와 값이 추가가 됨
print(student2)
student2['연락처']='010-4321-4321' #해당 키에 값이 있는 경우 값을 변경 함
print(student2)

##student2.append('010-1234-1234') ##AttributeError: 'dict' object has no attribute 'append'
##딕셔너리는 remove(), append() 함수를 적용할 수 없다

student2.pop('전공')      ##pop함수로 해당하는 키의 값 삭제
print(student2)
del(student2['이름'])      ##del 함수로 해당하는 키의 값 삭제
print(student2)

student2.clear()            ##clear로 딕셔너리 와 리스트의 내용 삭제 가능
print(student2)
student1.clear()
print(student1)

##mytuple.clear()                 ## 'tuple' object has no attribute 'clear' 튜플은 클리어로 삭제 불가
del(mytuple)
print(mytuple)                      ##NameError: name 'mytuple' is not defined
                                             ##튜플 자체를 삭제하여 mytuple을 찾을 수 없음













































