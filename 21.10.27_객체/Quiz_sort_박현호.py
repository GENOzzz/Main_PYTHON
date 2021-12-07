
aa=[]
a=int(input("리스트의 크기를 정해주십시오."))

for i in range(a):
    aa.append(int(input(str("%d번째의 정수를 입력해 주십시오"%i))))

for j in range(a):         ##리스트길이(a)만큼 반복 j를 키우면서
    k = a - j              ##k는 a-j로 명명
    for i in range(1, k):  ##1부터 시작해서 k번까지 반복 i를 키우면서
        if aa[i-1] >= aa[i]:     ##aa[i-1]수와 aa[i]번째수를 비교하여
                                 ## temp=aa[i]
            aa[i],aa[i-1] = aa[i-1],aa[i]   ##aa[i]=aa[i-1]          
                                            ##aa[i-1]=aa[i]의 세줄을 줄인것과 같음.(자리교체)
                                            ##temp없이 두줄만 쓰면 서로 값이 비워져 불가능.

print(aa)



    

