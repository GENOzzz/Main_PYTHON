from homemodule import *


while True:
    b=input("리스트를 작성하시겠습니까?  (yes y: , no :n )")
    if b=='y':
        list1=[]
        try : 
            for i in range(4):
                list1.append(int(input(str(i+1)+"번째 숫자를 입력해 주세요.")))   

            print(list1)
            print("해당 리스트 에서 최대값은 : ",maxmum(list1))
            print("해당 리스트 에서 최소값은 : ",minmum(list1))

        except ValueError :                                   
                    print("숫자만 입력해 주십시오")
                    continue

    elif b=='n':
        print("프로그램을 종료합니다.")
        break

