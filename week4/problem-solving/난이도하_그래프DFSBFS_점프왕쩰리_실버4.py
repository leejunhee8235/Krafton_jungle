# # 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# # 문제 링크: https://www.acmicpc.net/problem/16173
# 문제
# ‘쩰리’는 점프하는 것을 좋아하는 젤리다. 
# 단순히 점프하는 것에 지루함을 느낀 ‘쩰리’는 새로운 점프 게임을 해보고 싶어 한다. 
# 새로운 점프 게임의 조건은 다음과 같다.

# ‘쩰리’는 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 움직일 수 있다. 
# ‘쩰리’가 정사각형 구역의 외부로 나가는 경우엔 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
# ‘쩰리’의 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
# ‘쩰리’가 이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
# ‘쩰리’가 가장 오른쪽, 가장 아래 칸에 도달하는 순간, 그 즉시 ‘쩰리’의 승리로 게임은 종료된다.
# ‘쩰리’가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다. 
# 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.
# 새로운 게임이 맘에 든 ‘쩰리’는, 계속 게임을 진행해 마침내 최종 단계에 도달했다. 
# 하지만, 게임을 진행하는 구역이 너무 넓어져버린 나머지, 이 게임에서 이길 수 있는지 없는지 가늠할 수 없어졌다. 
# ‘쩰리’는 유능한 프로그래머인 당신에게 주어진 구역에서 승리할 수 있는 지 알아봐 달라고 부탁했다. 
# ‘쩰리’를 도와 주어진 게임 구역에서 끝 점(오른쪽 맨 아래 칸)까지 도달할 수 있는지를 알아보자!

# 입력
# 입력의 첫 번째 줄에는 게임 구역의 크기 N (2 ≤ N ≤ 3)이 주어진다.

# 입력의 두 번째 줄부터 마지막 줄까지 게임판의 구역(맵)이 주어진다.

# 게임판의 승리 지점(오른쪽 맨 아래 칸)에는 -1이 쓰여있고, 나머지 칸에는 0 이상 100 이하의 정수가 쓰여있다.

# 출력
# ‘쩰리’가 끝 점에 도달할 수 있으면 “HaruHaru”(인용부호 없이), 
# 도달할 수 없으면 “Hing” (인용부호 없이)을 한 줄에 출력합니다.

# n = int(input())
# board = [list(map(int,input().split())) for _ in range(n)]

# visited = [[False]*n for _ in range(n)]

# def dfs(x, y):
#     # 조건
#     #범위를 벗어나면 실패
#     if x < 0 or x>= n or y < 0 or y>=n:
#         return False
#     #이미 방문한 칸이면 다시 볼 필요 없음
#     if visited[x][y]:
#         return False
#     #도착점이면 성공
#     if x == n -1 and y == n - 1:
#         return True
    

#     visited[x][y] = True

#     jump = board[x][y]

#     #오른쪽 또는 아래로 이동
#     # 재귀
#     return dfs(x, y+jump) or dfs(x+jump,y)
# if dfs(0,0):
#     print("HaruHaru")
# else:
#     print("Hing")
import sys
input = sys.stdin.readline

# 게임 구역의 크기 (nxn 보드)
n = int(input())

# input().spilt() 한줄입력 공백으로 나눈후 map(int,) 문자열들을 정수로 바꾸고 list() 리스트에 집어넣고 
# 이걸 n번 반복해서 보드의 각 줄을 입력받아서 보드를 완성
board = [list(map(int,input().split()))for _ in range(n)]

# 보드의 방문여부주소 초기 False로 nxn 보드주소 입력
visited = [[False]*n for _ in range(n)]

# dfs 함수 시작
def dfs(x,y):
    # 조건
    # x와 y가 0보다 작거나 n보다 크거나 같을시에 범위를 벗어나기에 실패를 리턴
    if x < 0 or x>= n or y<0 or y>=n:
        return False
    # 방문여부주소에서 방문이 되어있으면 다시 볼 필요없기에 실패를 리턴
    if visited[x][y]:
        return False
    # 현재 위치가 도착점(오른쪽 아래 칸)이면 성공
    if x == n-1 and y == n-1:
        return True
    
    # visited[x][y] 가 현재 칸을 방문했다고 표시
    visited[x][y] = True

    # 점프는 보드의 값만큼 움직이기에 점프를 보드의 값으로 초기화
    jump = board[x][y]
    
    # 재귀 호출
    # 처음 시작부터 재귀를 써서 도착점까지 가게하기
    return dfs(x,y+jump) or dfs(x+jump, y)

if dfs (0,0):
    print("HaruHaru")
else:
    print("Hing")