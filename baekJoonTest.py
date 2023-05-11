C = int(input())
N = int(input())

graph = [[] for _ in range(C + 1)]
visited = [False] * (C + 1)

for i in range(N) : 
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited) :
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,i,visited)



print(graph)
dfs(graph,1,visited)
print(visited.count(True) -1)

