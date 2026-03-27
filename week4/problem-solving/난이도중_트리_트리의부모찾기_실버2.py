# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 노드 개수 입력
N = int(input())

# 그래프 생성 (1번부터 N번까지 쓰려고 N+1)
graph = [[] for _ in range(N + 1)]

# 간선 입력
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 부모를 저장할 배열
parent = [0] * (N + 1)

def dfs(node):
    for next_node in graph[node]:
        # 아직 부모가 정해지지 않은 노드라면
        if parent[next_node] == 0:
            parent[next_node] = node   # 현재 노드가 부모
            dfs(next_node)

# 루트는 1번
parent[1] = -1   # 루트 표시용
dfs(1)

# 2번 노드부터 N번 노드까지 부모 출력
for i in range(2, N + 1):
    print(parent[i])
