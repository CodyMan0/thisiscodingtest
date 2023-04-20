# N * M 크기의 직사각형 
# 동빈이 위치 (1,1) 출구 (N,M)
# 괴물 0 , 없는 부분 1 
# 탈출하기 위해 움직여야하는 최소 칸의 갯수 
# 시작 칸과 마지막칸을 모두 포함해서 계산한다. 

# 입출력 조건
# 4 <= N,M <= 200

# 자료구조
# BFS (가까운 노드부터 차례대로 그래프의 노드를 탐색하기에 )

from collections import deque

n,m = map(int, input().split())

# 2차원 배열 자료 구조
graph = []
for i in range(n) :
    graph.append(list(map(int,input())))

dx = [-1 , 1 , 0 , 0]
dy = [0 , 0, -1 , 1]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    while queue :
        print('before',queue)
        x,y = queue.popleft()
        print('after',queue)
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            print('infor',nx,ny)

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0 :
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                print('다음 순번',graph[nx][ny])
                queue.append((nx,ny))
    return graph[n -1][m -1]


print(bfs(0,0))
print(graph) # [[3, 0, 5, 0, 7, 0], [2, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 8], [14, 13, 12, 11, 10, 9], [15, 14, 13, 12, 11, 10]]
