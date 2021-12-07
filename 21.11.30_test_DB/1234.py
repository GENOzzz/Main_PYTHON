j=0
for i in range(0,10,1):
    for k in range(0,10,2):
        j+=1
        print(j)

my=["0","1","2","3","4","5","6"]
print(my[3:5])

mylist=[]
for i in range(0,100):
    mylist.append(0)
print(len(mylist))
print(mylist)


i,hap=0,0
for i in range(100,200,2):
    hap+=i
    print(i)
    print(hap)

a=1
while(a<=3):
    print("파이썬은 인간적인 언어이다 ㅇ")
    a+=1

print("ooooooooooooooo")

for i in range(0,3,1):
    print("파이썬은 인간적인 언어이다.")

b=''
l=['a','b','c']
b.join(l)
j=b.join(l)
jj=b.join(reversed(l))
print(j)
print(jj)
