# 다이내믹 프로그래밍은 아직 어떻게 푸는지 모르겠다. 
## array는 초기 금광 정보 
## dp 변수는 동적 계획을 위한 2차원 테이블

## dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j -1] , dp[i + 1][j - 1 ])

for tc in range(int(input())) :
    n,m = map(int,input().split())
    array = list(map(int, input().split()))

    dp = [ ]
    index = 0
    for _ in range(n):
        dp.append(array[index : index + m])
        index += m

    for j in range(1, m): 
        for i in range(n):
            if i == 0 :
                left_up = 0
                
            else :
                left_up = dp[i-1][j-1]

            if i == n-1 :
                left_down = 0
            else :
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    
    print('res',result)


