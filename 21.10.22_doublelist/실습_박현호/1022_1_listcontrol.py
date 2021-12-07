'''
myList=[30,10,20]
print("현재 리스트 : %s"%myList)

myList.append(40) ##리스트의 끝자리에 추가하는 함수.
print("append(40) 후의 리스트 : %s" %myList)

print("pop()으로 추출한 값 : %s" %myList.pop()) ##리스트 끝자리 부터 자동출력
print("pop() 후의 리스트 : %s : " % myList)

myList.sort()
print("sort() 후의 리스트 : %s" %myList) ##리스트 항목정렬 (오름차순)

myList.reverse()
print("revers() 후의 리스트 : %s" %myList)

print("index()로 찾은 20 값의 위치 : %d" %myList.index(20))

myList.insert(2,222)
print("insert(2,222) 후의 리스트 : %s" %myList) ## 리스트 2번째자리에 222를 넣어라.

myList.remove(222)
print("remove(222) 후의 리스트 : %s" %myList)

myList.extend([77,88,77])
print("extend([77,88,77]) 후의 리스트 : %s" %myList)

print("count()로 찾은 77 값의 개수 : %d" %myList.count(77))
'''
'''
aa=[]
bb=[]
n=0

for i in range(100):            ##aa리스트에 0번째자리에 0부터시작해서 2씩 증가시키면서 넣겠다.
    aa.append(n)
    n+=2

for i in range(100):            
    bb.append(aa[99-i])     ##bb리스트는 aa리스트의 역순으로 0번째부터 넣겠다.
    
print("aa[0]은 %d, aa[99]는 %d 입력됨" %(aa[0], aa[99]))
print("bb[0]은 %d, bb[99]는 %d 입력됨" %(bb[0], bb[99]))
''''

aa=[]
aa=[10,20,30]
aa[1:2]=[100,200]

aa
