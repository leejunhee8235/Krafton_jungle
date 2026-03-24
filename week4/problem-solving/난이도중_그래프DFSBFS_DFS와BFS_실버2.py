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
from collections import deque
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

dfs_result = []

def dfs(v):
    visited[v] = True
    dfs_result.append(v)
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

dfs(V)


# bfs 구현
bfs_result = []
bfs_visited = [False]*(N+1)

def bfs(start):
    queue = deque()

    # 큐에 시작 정점을 넣고 방문처리하기
    queue.append(start)
    bfs_visited[start] = True




    # 큐가 빌때까지
    while queue:
        v = queue.popleft()

        bfs_result.append(v)

        for bfs_next in graph[v]:

            if not bfs_visited[bfs_next]:
                bfs_visited[bfs_next] = True
                queue.append(bfs_next)
bfs(V)


# bfs_result = []
# bfs_visited = [False] * (N + 1)

# def bfs(start):
#     # 큐 생성
#     queue = deque()
    
#     # 시작 정점을 큐에 넣고 방문 처리
#     queue.append(start)
#     bfs_visited[start] = True
    
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐의 맨 앞 정점을 꺼냄
#         v = queue.popleft()
        
#         # 꺼낸 정점을 방문 순서에 저장
#         bfs_result.append(v)
        
#         # 현재 정점과 연결된 정점들을 확인
#         for nxt in graph[v]:
#             # 아직 방문하지 않은 정점이면
#             if not bfs_visited[nxt]:
#                 # 방문 처리하고 큐에 넣음
#                 bfs_visited[nxt] = True
#                 queue.append(nxt)

# # BFS 시작
# bfs(V)

print(*dfs_result)
print(*bfs_result)