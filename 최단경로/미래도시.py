# 문제의 n, 즉 노드의 범위가 0이상 100이하로 매우 한정적이기에 O(n^3)인
# 플로이드 워셜 알고리즘을 활용해서도 빠르게 풀 수 있다.

# 나에게 적용할 것 먼저 그래프 그림 그려보기!!

# 입력
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5


# # 책 풀이
# INF = int(1e9)
# n,m = map(int,input().split())
# graph = [[INF] * (n + 1) for _ in range(n + 1)]

# for a in range(1, n + 1) :
#     for b in range(1, n + 1) :
#         if a == b :
#             graph[a][b] == 0

# for _ in range(m) :
#     a , b = map(int,input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# x , k = map(int, input().split())

# for k in range(1, n + 1) :
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[b][k])

# distance = graph[1][k] + graph[k][x]

# if distance >= INF :
#     print('-1')
# else:
#     print(distance)
    



# ## 30분 고민하다가 풀이를 보고 이해해보기로...



# 책 풀이
INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if a == b :
            graph[a][b] == 0

for _ in range(m) :
    a , b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x , k = map(int, input().split())

for k in range(1, n + 1) :
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[b][k])

distance = graph[1][k] + graph[k][x]

if distance >= INF :
    print('-1')
else:
    print(distance)
    



## 30분 고민하다가 풀이를 보고 이해해보기로...