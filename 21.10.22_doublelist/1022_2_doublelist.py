list1=[ ]                               ##내부배열(1차원)
list2=[ ]                               ##외부배열(2차원)
list3=[ ]                               ##외부의 외부배열 (3차원)
value=1                              ## i나 k 는 for문에서 0으로 초기화가 되기때문에 0에서 부터 시작함.
                                            ##∴배열의 값을 위한 초기화 되지않는 변수 선언

for x in range(3):                   ##층을 설정하기위한 반복문(3번반복
    for i in range(0,4):             ## 외부배열을 위한 반복문 (4번반복
        for k in range(0,5):        ## 내부배열을 위한 반복문 (5번반복
            list1.append(value)   ##list1에 1씩 증가하는 value값을 쌓음
            value+=1
        list2.append(list1)         ##list2에 list1을 추가해라.
        list1=[  ]                           ##list1을 비워라.
    list3.append(list2)             ##list3에 list2를 추가해라
    list2=[]                                ##list2를 비워라                        ##배열이 쌓이고 비워지기를 반복하여
    print(list3)                                                                               ##결과적으로 list3에 순차적으로 list1과 list 2가 쌓임


'''    
for i in range(0,3):             ##2차원 리스트의 값을 출력하기
    for k in range(0,4):
        print("%3d"%list2[ i ][ k ],end=" ")        ##하나하나 출력하기 = 열과 행을 구분하여.
    print("")                                                       ##시스템 상으로 한줄로 나오는게 맞음.
'''
'''
for i in range(9):
    list1.append(i+1)

print(list1)
'''
'''
for i in range(3):                  
    for k in range(4):
        list1.append(value)
        value+=1
    list2.append(list1)
    list1=[]                                ##비워주지 않으면 list1에 누적하여 값이 쌓임 [1,2,3,4,5,6,7,8.....]
    print(list1)
    print("")
    print(list2)
    print("")
'''  

