# 요약

## 1. 공유기 사이 거리를 x로 설정
## 2. x를 기준으로 공유기를 설치
## 3. 공유기를 C개 이상 설치할 수 있다.

# 입력 
# 5 3
# 1
# 2
# 8
# 4
# 9
# 10억이라는 수는 이분 탐색으로 밖에 해결 못하기에 힌트가 될 수 있다. 

n, c = list(map(int,input().split(' ')))

array = []

for _ in range(n) :
    array.append(int(input()))
array.sort()

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while (start <= end) :
    mid = (start + end) // 2
    print('e',start,end)
    value = array[0]
    count = 1
    
    for i in range(1, n) :
        print('i',i)
        if array[i] >= value + mid :
            # 첫번째와 미드값을 더했을때
            # array[i]보다 작으면
            value = array[i]
            count += 1
    if count >= c :
        start = mid + 1
        result = mid
    else :
        end = mid - 1

print(result)