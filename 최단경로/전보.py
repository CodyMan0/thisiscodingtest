# 어떤 나라에는 N개의 도시 

# X -> Y로 보내려면 통로가 있어야한다. 

# 어느날 C라는 도시 위급 , 최대한 많은 도시로 메시지 보내려고 할때
# 출발이 C에서 시작해서 메시지를 맏는 도시의 총 개수와 시간은 얼마나


# 입력 
# 첫번째 도시 개수(N) 1이상 30000, 통로 개수(M) 1이상 20만 이하, 메시지 타겟 도시 C는 1이상 30000이하
# M + 1 번째부터 통로에 대한 X , Y, Z 

# 출력 
# C로 부터 받은 도시의 갯수와 최댓값인 시간을 리턴


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())

graph = [[]for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m) :
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for node in graph[now] :
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q,(cost,node[0]))

dijkstra(start)

count = 0
max_distance = 0 

for i in distance:
    if i != INF :
        count += 1
        max_distance = max(max_distance, i)

print(count - 1, max_distance)        
    




