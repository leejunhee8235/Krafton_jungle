"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    # 그래프를 인접 리스트로 저장할 리스트
    # 예: graph[0] = [1, 2] 이면 0 -> 1, 0 -> 2
    graph = [[] for _ in range(vertices)]
    # 각 정점의 진입 차수 저장
    # in_degree[i] = i번 정점으로 들어오는 간선 수
    in_degree = [0]*vertices
    
    # TODO: 그래프 구성 및 진입 차수 계산
    # 간선 정보를 바탕으로 그래프 구성
    # 그리고 도착 정점의 진입 차수를 1 증가
    for u, v in edges:
        graph[u].append(v)  # u -> v 연결
        in_degree[v] += 1   # v로 들어오는 간선 1개 추가
    
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    queue = deque()
    # 처음부터 바로 시작 가능한 정점(진입 차수 0)을 큐에 넣기
    for i in range(vertices):
        if in_degree[i] == 0:
            queue.append(i)
    # 위상 정렬 결과를 저장할 리스트
    result = []
    
    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소
    while queue:
        # 현재 진입 차수가 0인 정점을 꺼냄
        current = queue.popleft()
        # 결과에 추가
        result.append(current)
        # current와 연결된 다음 정점들을 확인
        for neighbor in graph[current]:
            # current를 제거한 효과로 neighbor의 진입 차수를 1 감소
            in_degree[neighbor] -= 1
            # 진입 차수가 0이 되면 이제 처리 가능하므로 큐에 추가
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
## 꼭 다시 한번 보기