# 주어진 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘을 만들어 보세요.
# 리스트에 들어 있는 숫자를 크기 순으로 나열하는 정렬 알고리즘의 입출력

# 2. 쉽게 설명한 선택 정렬
# 정렬 원리를 이해하기 위한 참고용 프로그램
# 입력: 리스트 a, 출력: 리스트 result, 정렬된 새 리스트
a = [2, 4, 5, 1, 3] # 주어진 리스트
result = []  # 새 리스트를 만들어 정렬된 값을 저장
print("a",a)
print("result",result)

while a:     # 주어진 리스트에 값이 남아있는 동안 계속
    n = len(a)  # 반복할 때마다 길이 줌어듦
    min_idx = 0 # 최소값 인덱스, 반복할 때마다 초기값 0번째로 지정
    #주어진 리스트에서 최솟값의 위치를 돌려주는 반복문
    for i in range(1, n):           # 남은 자료 중에서 최솟값의 위치를 찾음 
        if a[i] < a[min_idx]:
            min_idx = i
    value = a.pop(min_idx)  # 찾은 최솟값을 a 에서 삭제하고 value에 저장
    result.append(value)     # value를 결과 리스트 result 끝에 추가
    print("min_idx", min_idx)
    print("a",a)
    print("result",result)
print("선택 정렬 알고리즘 결과",result)
