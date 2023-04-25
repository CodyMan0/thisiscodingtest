# 입력 
# 식량 창고의 갯수 (3이상 100이하)
# 둘째줄 공백으로 구분되어 식량창고에 저장된 식량의 갯수 K 

# 출력 
# 최댓값
n = int(input())

array = list(map(int,input().split()))

dp  = [0] * (n+1)

dp[0] = array[0]
dp[1] = max(array[0], array[1])
for i in range(2,n) :
    dp[i] = max(dp[i-1], dp[i-2] + array[i])


print(dp[n-1])


# 중요
# 점화식 a = max(a i-1 , a i-2 + ki)을 그대로 코드에 옮긴 것.
# 동적 프로그래밍이 성립되기 위해선 큰 문제를 작은 문제로 나눌 수 있으면 된다.
# 이런 차원에서 분할 정복 알고리즘과 차이가 거론되는 것 같다.



