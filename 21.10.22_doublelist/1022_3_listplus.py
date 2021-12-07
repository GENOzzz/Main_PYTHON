aa=[]
bb=[]
n=1

for i in range (4):
    for k in range(4):
        aa.append(i)

    bb.append(aa)
    aa=[]

    print(bb)



