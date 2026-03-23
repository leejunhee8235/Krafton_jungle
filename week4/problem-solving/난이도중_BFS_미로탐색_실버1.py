# # BFS - 미로 탐색 (백준 실버1)
# # 문제 링크: https://www.acmicpc.net/problem/2178

# 문제
# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, 
# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 
# 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 
# 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# N개의줄에 M개의 정수 1,2 -> 1 0 1,3-> 1 0 1
# 0은 이동할 수 없는 칸 1은 이동할 수 있는 칸
# (1,1)출발 (N,M)도착
# 도착까지 최소 칸 수 구하기
# import sys
# input = sys.stdin.readline

# N,M = map(int, input().split())
# miro = [list(map(int,input().strip())) for _ in range(N)]

# visited = [[False]*M for _ in range(N)]
# khan = 0

# def dfs(x,y):
 #    if x < 0 or x >= M or y <0 or y >= N:
#         return
#     if visited[x][y]:
#         return
#     if miro[x][y] == 0:
#         return

    
#     visited[x][y] = True

#     dfs(x-1,y)
#     dfs(x+1,y)
#     dfs(x,y-1)
#     dfs(x,y+1)

#     for i in range(M):
#         for j in range(N):
#             if miro[x][y] == 1 and not visited[x][y]:
#                 khan+=1
#                 dfs(i,j)

#     return khan

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
miro = [list(map(int,input().strip())) for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0,0)) # 시작점

    # 상하좌우 이동
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        # 큐의 맨 앞 좌표(현재위치)를 꺼내서 x,y에 저장
        x,y = queue.popleft()

        # 현재위치에서 상하좌우 방향을 차례대로 확인
        for i in range(4):
            # 다음에 이동할 좌표 계산
            # 현재 위치에 방향값을 더함
            nx = x+dx[i] #0123  0,-1 0,1 0,0 0,0
            ny = y+dy[i]

            #범위 밖이면 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            #벽(0)이면 못감
            if miro[nx][ny] == 0:
                continue

            #아직 방문 안 한 길(1)이면 
            if miro[nx][ny] == 1:
                # 다음 칸까지의 거리 = 현재 칸까지의 거리 + 1
                miro[nx][ny] = miro[x][y] +1
                # 새로 방문한 칸을 큐에 넣음
                queue.append((nx,ny))

    return miro[N-1][M-1]

print(bfs())


