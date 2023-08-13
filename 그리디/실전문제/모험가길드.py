#1회
## 첫번째 시도 X 
## 핵심은 정렬


n = int(input())
array = list(map(int,input().split()))
array.sort()

result = 0
count = 0

print(array)
for horror in array :
    count += 1
    if count >= horror :
        result += 1
        count =0
    print(horror,result,count)

print(result)
