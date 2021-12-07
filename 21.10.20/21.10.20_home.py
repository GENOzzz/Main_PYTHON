def maxmum(a):              ##함수 maxmum(a)정의
    maxmum=a[0]             ## 변수 선언 : maxmum에 a리스트의 [0]번째로 변수 대
    for i in a:             ##변수 i는 리스트 만큼 반복하면서 a[i]번째 값을 대입 시킨다.
        if maxmum<i:        ##만약 i가 minmum보다 작을경우
            maxmum=i        ##maxmum은 i로 교체된다.
    return maxmum           ##a리스트를 순차탐색한 후 최종 maxmum값 반환

def minmum(a):              ##함수 minmum(a)정의
    minmum=a[0]             ##변수선언 : minmum에 a리스트의 [0]번째로 변수 대입
    for i in a:             ##변수 i는 리스트 만큼 반복하면서 a[i]번째 값을 대입 시킨다.
        if minmum>i:        ##만약 i가 minmum 보다 작을경우
            minmum=i        ##minmum은 i로 교체된다.
    return minmum           ##a리스트를 순차탐색한 후 최종 minmum값 반환

list1=[]

for i in range(10):
    list1.append(int(input(str(i+1)+"번째 숫자를 입력해 주세요.")))

print(list1)
print("최대값은 : ",maxmum(list1))
print("최소값은 : ",minmum(list1))

