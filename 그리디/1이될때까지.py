# n이 1이 될 때까지 두 과정 중 하나를 반복적으로 수행한다.
# 단 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다. 

# 내 정답
n , k = map(int, input().split())
result = 0

while n > 1 : 
    if n % k == 0 :
        n = n / k 
        result += 1
    else :
        n = n - 1
        result += 1

print(result)