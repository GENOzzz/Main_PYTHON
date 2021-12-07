def ssss(list,x):
    n=len(list)
    r=0
    for i in range(n):
        if x == list[i]:
            return i
        elif x!=list[i]:
            return r++


aa=[]
while True:
    b=input("리스트를 작성하시려면 y를 입력해 주십시오.")
    try:

        if str(b)=='y':
            x=int(input(("리스트의 크기를 정해주십시오.")))

            for i in range(x):
                aa.append(int(input(str(i)+"번째 숫자를 입력해 주십시오 :")))

            print(aa)

            a=int(input("탐색할 값을 입력해 주십시오 :"))

            if not a in aa:
                print("해당숫자는 리스트에 존재하지 않습니다.")

            else:
                ssss(aa,a)
                print("%d의 위치는 [%d]번째 입니다." %(a,ssss(aa,a))

        elif str(b)!='y':
            print("프로그램을 종료합니다.")
            break
