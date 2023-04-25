# 입력 정수 X 
# 출력 연산을 하는 횟수의 최솟값을 출력 

# 2,3,5로 나누어떨어지면 나누고 X에서 1을 뺸다. 그래서 1을 만들려고 할떄 
# 연산 최소 

x = int(input())

dp = [0] * (x+1)

for i in range(2, x + 1):
    
    dp[i]  = dp[i-1] + 1
    if i % 2 == 0 :
        dp[i] = min(dp[i],dp[i // 2] + 1)
    if i % 3 == 0 :
        dp[i] = min(dp[i],dp[i // 3] + 1)
    if i % 5 == 0 :
       dp[i] = min(dp[i],dp[i // 5] +  1)

print(dp[x])

