# # 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# # 문제 링크: https://www.acmicpc.net/problem/11724

# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
# (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

import sys
input = sys.stdin.readline

# 첫 줄에서 정점 개수 N, 간선 개수 M 입력
N, M = map(int, input().split())

# 그래프를 인접 리스트로 만들기
# 정점 번호가 1번부터 N번까지라서 N+1 크기로 만듦
# 0번 인덱스는 사용하지 않음
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
# 무방향 그래프이므로 u -> v, v -> u 둘 다 저장
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부를 저장하는 리스트
# 처음엔 아무 정점도 방문하지 않았으므로 전부 False
visited = [False] * (N + 1)

# DFS 함수
# v: 현재 방문 중인 정점 번호
def dfs(v):
    # 현재 정점을 방문 처리
    visited[v] = True

    # 현재 정점과 연결된 모든 다음 정점을 확인
    for next_node in graph[v]:
        # 아직 방문하지 않은 정점이면
        if not visited[next_node]:
            # 그 정점으로 계속 DFS 진행
            dfs(next_node)

# 연결 요소 개수를 셀 변수
count = 0

# 1번 정점부터 N번 정점까지 하나씩 확인
for i in range(1, N + 1):
    # 아직 방문하지 않은 정점이라면
    # 새로운 연결 요소가 시작된다는 뜻
    if not visited[i]:
        # 그 정점에서 DFS를 시작해서
        # 같은 연결 요소에 속한 정점들을 전부 방문 처리
        dfs(i)

        # DFS를 한 번 시작했다 = 연결 요소를 하나 찾았다
        count += 1

# 최종 연결 요소 개수 출력
print(count)