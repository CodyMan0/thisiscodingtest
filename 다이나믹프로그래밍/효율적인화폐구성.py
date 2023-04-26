# 입력
# n은 100이하 m은 10000이하 

# 출력
# 최소한의 화폐개수 
# 불가능 -1 

# 책 풀이 
n,m = map(int, input().split())
array=[]
for i in range(n):
    array.append(int(input()))

dp = [10001] * (m+1)

dp[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        dp[j]= min(dp[j],dp[j- array[i]] + 1)

if dp[m] == 1001 :
    print(-1)
else :
    print(dp[m])



# 와 이걸 어떻게 푸는지 모르겠지만 우선 이해하고 넘어가자 .
# 아직은 막히지만 낙심하지말고 공부하자