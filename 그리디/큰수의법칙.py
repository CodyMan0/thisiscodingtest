n,m,k = map(int,input().split())
array = list(map(int,input().split()))

array.sort(reverse=True)
first = array[0]
second = array[1]


result = 0

while True:
    for i in range(k) :
        print(m)
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)


# 나의 생각
# 4.17 약 5일간 독감으로 앓다가 정신을 차라기 위해 풀어본 그리디 알고리즘... 유난히 지치고 하기 싫은 날이다.
