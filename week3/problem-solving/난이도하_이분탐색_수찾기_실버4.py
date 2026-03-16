# # 이분탐색 - 수 찾기 (백준 실버4)
# # 문제 링크: https://www.acmicpc.net/problem/1920
# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

N = int(input())  # 첫째 줄: 숫자 개수 N 입력

A = list(map(int, input().split()))  # 둘째 줄: N개의 정수를 공백 기준으로 나눠 리스트로 저장

M = int(input())  # 셋째 줄: 찾을 숫자 개수 M 입력

targets = list(map(int, input().split()))  # 넷째 줄: 실제로 찾아볼 숫자들을 리스트로 저장

A.sort()  # 이분 탐색을 하려면 정렬이 필요하므로 A를 오름차순 정렬

for target in targets:  # 찾아볼 숫자들을 하나씩 꺼내서 검사
    left = 0  # 탐색 시작 위치(맨 왼쪽 인덱스)
    right = len(A) - 1  # 탐색 끝 위치(맨 오른쪽 인덱스)
    found = 0  # 아직 target을 못 찾았다고 가정하고 0으로 시작

    while left <= right:  # 탐색 범위가 남아 있는 동안 반복
        mid = (left + right) // 2  # 현재 탐색 범위의 중간 인덱스 계산

        if A[mid] == target:  # 중간값이 찾는 값과 같으면
            found = 1  # 찾았으므로 1로 표시
            break  # 더 볼 필요 없으니 while문 종료

        elif A[mid] < target:  # 중간값이 찾는 값보다 작으면
            left = mid + 1  # target은 오른쪽에 있으므로 left를 mid 다음으로 이동

        else:  # 위 두 경우가 아니면 A[mid] > target 이라는 뜻
            right = mid - 1  # target은 왼쪽에 있으므로 right를 mid 이전으로 이동

    print(found)  # 찾았으면 1, 못 찾았으면 0 출력