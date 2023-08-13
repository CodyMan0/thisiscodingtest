


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


# from collections import deque

# n , m = map(int, input().split())


# # 그래프 생성
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# # 상하좌우 탐색 (북 , 남 , 동 , 서 )
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# # BFS가 우선 떠올랐다
# def bfs(x,y) : 
#     q = deque()
#     q.append((x,y))

#     # 조건 
#     if graph[x][y] == 1 : 
#         return False

#     while q : 
#         x,y = q.popleft()
#         graph[x][y] = 1

#         # 4방향 탐색
#         for i in range(4) :
#             nx = x + dx[i]
#             ny = y + dy[i]
            
#             print('q',q)
#             # 지정된 얼음판 위치에 부합하면 큐에 넣는 로직
#             if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0 :
#                 q.append((nx,ny))
            
#     return True

# cnt = 0

# for i in range(n):
#     for j in range(m):
#         if bfs(i,j) == True : 
#             print(i,j)
#             cnt += 1
#             print(cnt)

# print(cnt)
