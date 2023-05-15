## 그래프

그래프는 NODE(vertex)와 EDGE으로 표현된다. 표현방식에는 2가지가 존재한다: 인접행렬/인접리스트

1.  인접행렬 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식으로 2차원 리스트를 이용한다./ 연결되어 있지 않은 노드끼리는 무한의 비용이라고 작성한다

    필요없는 노드관계도 다 저장해, 노드 개수가 많을 수록 메모리가 낭비

```python
INF=99999999999
graph=[[0,7,5],[7,0,INF],[5,INF,0]]
print(graph)
```

2.  인접리스트 리스트자료형을 이용해 기록하는 방식으로 연결된 노드 정보만 (노드,거리)로 전달한다. 인접행렬에 비해 메모리가 효율적이지만, 특정 두 노드가 연결되어있는지 확인하는데 오래걸려 따라서, 특정노드에 연결된 모든 인접 노드를 순회해야하는 경우 인접 리스트 방식이 인접행렬보다 메모리 낭비가 적다.

```python
graph=[[] for _ in range(3)]

#노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

#노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)
```

# 백트래킹이란?
모든 경우의 수를 고려하는 알고리즘으로써, 상태공간을 트리로 나타낼 수 있을때 적합하다. 방식에 따라 DFS, BFS등이 있다. 
(DFS,BFS가 백트레킹 알고리즘의 하위 개념이었구나!)

## 두가지 알고리즘 예시

- bfs 사용하기 적합한 때

1. 모든 간선의 비용이 동일할때 (특정 거리의 도시 찾기)

## DFS

DFS는 stack을 이용해 다음과 같은 로직으로 진행된다. 탐색에 O(N)이 걸린다.

1.  탐색 시작 노드를 스택에 넣고 **방문 처리**를 한다.
2.  스택의 최상단 노드에 방문하지 않은 인접노드가 있으면 인접노드를 스택에 넣고 방문처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3.  2번을 더 이상 수행할 수 없을 때까지 반복한다.

위와 같은 방식을 구현하는데 재귀함수를 아래와 같이 구현할 수 있다.

```python
def dfs(graph,v,visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v] :
        if not visited[i]:
            dfs(graph, i , visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph , 1 , visited)
```

## BFS

자료구조 큐를 활용하여 가까운 노드부터 탐색하는 알고리즘으로써 DFS와 반대의 알고리즘. 또한 탐색하는데 O(N)이 소요되고 일반적으로 DFS보다 약간 성능이 좋다는 점이 있다.

1.  탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
2.  큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리를 한다.
3.  2번을 더이상 수행할 수 없을 때까지 반복한다.

위의 로직을 아래와 같이 구현할 수 있다.

```python
from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph , 1 , visited)
```


### 사전 지식 : stack, queue , recursive function

stack : 선입 후출 구조 혹은 후입 선출 구조이다. 파이썬에서는 append와 pop 매소드가 동일하게 리스트의 말미에서 데이터를 삽입하고 삭제하기에 별다른 라이브러리를 사용할 필요가 없다.

queue: 선입 선출의 구조. 파이썬에서 큐를 구현하기 위해 deque라는 라이브러리를 사용할 수 있다. 핵심은 삽입과 삭제를 각각 다른 위치에서 시켜주면 되는 것.

resursive function : 자기 자신을 호출하는 함수로 기저 조건을 필히 기입해야한다.

- 예제 : 팩토리얼 구현하기

```python
# 탑 다운
def factorial_iterative(n):
	result = 1
	for i in range(1, n + 1)
		result *= i
	return result
# 바텀 업
def  factorial_iterative(n):
	if n <= 1:
	return 1
	return n * factorial_iterative(n - 1):

```

반복문의 방식보다 재귀함수를 사용했을때 코드가 더 간결해진다. 하지만 스택을 많이 차지하므로 성능에 좋지 않을때도 있다는 점 기억하자.


