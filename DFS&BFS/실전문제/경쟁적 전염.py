# # 여기서 핵심은 graph 리스트를 활용하여 data 리스트에 바이러스 정보를 
# # 정렬해서 담아넣는것.



# # BFS 사용 

# from collections import deque

# n,k = map(int,input().split())

# graph = []
# data =[]

# for i in range(n) :
#     graph.append(list(map(int,input().split())))
#     for j in range(n):
#         if graph[i][j] != 0: 
#             data.append((graph[i][j],0,i,j))

# print(data)


# data.sort()
# q = deque(data)


# target_s , target_y , target_x = map(int,input().split())

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# while q : 
#     virus,s,x,y =q.popleft()
#     if s == target_s :
#         break
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if 0 <= nx < n and 0<= ny < n:
#             if graph[nx][ny] == 0 :
#                 graph[nx][ny] = virus
#                 q.append((virus,s+1,nx,ny))

# print(graph[target_y -1][target_x -1])
        

# 두번째

from collections import deque

n,k = map(int,input().split())

graph = []
data =[]

for i in range(n) :
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0: 
            data.append((graph[i][j],0,i,j))

print(data)


data.sort()
q = deque(data)


target_s , target_y , target_x = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q : 
    virus,s,x,y =q.popleft()
    if s == target_s :
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0<= ny < n:
            if graph[nx][ny] == 0 :
                graph[nx][ny] = virus
                q.append((virus,s+1,nx,ny))

print(graph[target_y -1][target_x -1])
        