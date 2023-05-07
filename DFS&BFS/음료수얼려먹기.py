


# 문제
# N * M 크기의 얼음틀이 있다. 구멍은 0 칸막이가 존재하는 것은 1로 표시
# 구멍이 뚫려 있는 부분까리 상,하,좌,우로 붙어있는 경우 서로 연결되어 있는 것으로
# 간주한다. 이때 얼음 틀의 모양이 주어졌을때 성성되는 총 아이스크림의 갯수를
# 구하라 

# 연결 요소 찾기! 
# 1 < = n,m < 1000 

n , m = map(int, input().split())

# n이 세로 m이 가로 

graph = []
for i in range(n) :
    graph.append(list(map(int,input())))


def dfs(x,y) :
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False
    # 현재 노드 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1 , y)
        dfs(x , y - 1)
        dfs(x+1 , y)
        dfs(x , y + 1)
        return True
    return False

result = 0 

for i in range(n) :
    for j in range(m):
        print(n,m,dfs(i,j))
        if dfs(i,j) == True :
            print('세로',i ,'가로',j)
            result += 1

print(graph)


print(result)
