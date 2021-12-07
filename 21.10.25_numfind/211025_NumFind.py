aa=[]
c=0
a=int(input("리스트의 크기를 정해주십시오."))

for i in range(a):
    aa.append(int(input(str("%d번째의 정수를 입력해 주십시오"%i))))

print(aa)

b=int(input("찾으실 숫자를 입력해 주십시오."))

for i in range (a):
    if b==aa[i]:
        print("찾으시는 숫자는 %d번째에 있습니다."%i)

    elif b!=aa[i]:
        c+=1
        if c==a:
            print("%d(은)는 리스트에 없습니다."%b)
    

