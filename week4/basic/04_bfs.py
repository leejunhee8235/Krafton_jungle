"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited = []          # 최종적으로 방문한 순서를 저장할 리스트
    seen = set()          # 이미 방문했는지 확인하는 집합 (중복 방문 방지)
    # TODO: 큐 생성 및 시작 정점 추가
    ## 방문한 정점 집합
    queue = deque([start])  # 큐를 만들고, 시작 정점을 먼저 넣어둠
    seen.add(start)         # 시작 정점은 이미 방문 예정이므로 방문 표시
    
    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들 확인
    ## 방문하지 않은 정점이면 큐에 추가

    while queue:            # 큐에 방문할 정점이 남아 있는 동안 반복
        current = queue.popleft()  # 큐의 맨 앞 정점을 꺼냄 (가장 먼저 들어온 정점)
        visited.append(current)    # 꺼낸 정점을 방문 순서에 추가

        for neighbor in graph[current]:   # 현재 정점과 연결된 이웃 정점들을 하나씩 확인
            if neighbor not in seen:      # 아직 방문하지 않은 정점이라면
                seen.add(neighbor)        # 방문했다고 표시하고
                queue.append(neighbor)    # 나중에 탐색할 수 있도록 큐 뒤에 추가

    return visited        # BFS가 끝난 뒤 방문 순서 리스트 반환

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")

