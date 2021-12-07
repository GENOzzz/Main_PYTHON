'''
num = [1,8,7,3,2,-10,44,1,6,5]

print(min(num))
print(max(num))

aa=[]
for i in range(10):
    a=int(input(str(i+1)+ "번째 정수입력 : "))

    aa.append(a)
    aa=list(set(aa))

print(aa)
print("최대값은 %d" %max(aa))
print("최소값은 %d" %min(aa))
'''
##정해진 리스트에 최댓값 최솟값 찾는 코드
num=[1,889,7,3,552,-10,-444,1,6,5]

max_num = num[0]
min_num = num[0] 
 
for n in num:
    if max_num < n:
        max_num = n
 
    if min_num > n:
        min_num = n
 
print("최대값: ", max_num)
print("최소값: ", min_num)

##입력한 리스트에 최댓값 최솟값 찾는 코드
aa=[]

for i in range(8):  
    aa.append(0)                                                                                
    aa[i]=int(input(str(i+1) + "번째 숫자를 입력해 주세요 : "))

maxn=aa[0]
minn=aa[0]

for n in aa:
    if maxn<n:
        maxn=n

    if minn>n:
        minn=n

print(aa)
print("최대값 :",maxn)
print("최소값 : ",minn)

