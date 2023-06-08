# 숫자가 큰 자식 노드를 선택하면 합이 최대가 될까?
# 자식의 자식노드도 확인해야하는거 아닌가? 

# 한가지 조건
# 가장 큰 값을 자식들에게 다 더하면 될 것 같다. 

n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]
# m은 n이 1씩 증가할때 같이 증가한다. 



for i in range(1,n):
    for j in range(i + 1) :
        print('i',i,'j',j)
        if j == 0 :
            up_left=0
        else :
            up_left = dp[i -1][j -1]
        if j == i :
            up = 0
        else :
            up = dp[i - 1][j]
        dp[i][j] = dp[i][j] + max(up_left , up)

print(max(dp[n-1]))


# 문제를 풀면서 해결하지 못한 부분
## 왼쪽 위 혹은 바로위 2가지 위치에서만 내려오도록 하는것을 못함
## dp[i][j] = node[i][j] + max(dp[i - 1][j -1] , dp[i - 1][j])



## 풀이 
