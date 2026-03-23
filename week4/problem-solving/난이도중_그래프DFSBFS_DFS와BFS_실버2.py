# # 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# # 문제 링크: https://www.acmicpc.net/problem/1260
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
# V부터 방문된 점을 순서대로 출력하면 된다.

# DFS 결과 BFS 결과 정점 번호 작은것부터 첫째줄 정점 개수 간선 개수 탐색을 시작할 정점 번호
# 다음 M개의 줄에는 두 정점의 번호 무방향 그래프

# 4 정점 개수 5 간선 개수 1 정점 시작 번호  1 - 2   1 - 3 1 - 4 2 - 4  3 - 4
#DFS 1 - 2 - 4 - 3 ,BFS 1 - 2 - 3 - 4

import sys
input = sys.stdin.readline
# dfs 구현

N, M , V = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False]*(N+1)


result = []

def dfs(v):
    visited[v] = True
    result.append(v)
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

dfs(V)
print(*result)

# bfs 구현