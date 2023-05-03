#1회
## 첫번째 시도 X 
## 핵심은 정렬


n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0
count = 0

for i in data :
    count += 1
    if count >= i :
        result += 1
        count =0

print(result)
