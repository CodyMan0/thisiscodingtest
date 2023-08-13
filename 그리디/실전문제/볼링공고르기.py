# n 1이상 1000이하 m 1이상 10이하
# 무게 공백으로 구분 

# 첫번째 시도는 이중 포문

# n ,m = map(int,input().split())


# weight = list(map(int,input().split()))
# result = 0

# for i in  range(n) :
#     for j in range(i+1, n) :
#         if weight[i] != weight[j] :
#             result += 1

# print(result)

# 책 풀이 
## 아이디어 : 

n ,m = map(int,input().split())
weight = list(map(int,input().split()))

array = [0] * 11

for x in weight : 
    print(x)
    array[x] += 1


result = 0 

for i in range(1, m+1) :
    n = n - array[i]
    result += array[i] * n

print(result)

