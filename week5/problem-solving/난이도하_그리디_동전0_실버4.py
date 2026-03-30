# # 그리디 - 동전 0 (백준 실버4)
# # 문제 링크: https://www.acmicpc.net/problem/11047
# 문제
# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)

# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. 
# (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

# 출력
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

# 동전 종류 개수 N, 목표 금액 K 입력
# N,K = map(int,input().split())
# # 동전 가치들을 저장할 리스트
# A = []
# # 동전 가치를 N줄에 걸쳐 하나씩 입력받아 저장
# for _ in range(N):
#     A.append(int(input()))

# # 사용한 동전 개수의 총합
# result = 0

# #큰 동전부터 확인하기 위해 뒤에서부터 순회
# for coin in reversed(A):
#     # 현재 동전으로 K를 몇 개 사용할 수 있는지 계산
#     count = K // coin
#     # 사용한 동전 개수를 정답에 누적
#     result += count
#     # 현재 동전을 count개 사용하고 남은 금액만 남김
#     K -= coin * count

# print(result)

# N, K = map(int, input().split())
# coins = []
# for _ in range(N):
#     coins.append(int(input()))

# coins = coins[::-1]
# coin_count = 0

# for coin in coins:
#     curr_count = K // coin
#     if curr_count >= 1:
#         K -= (coin * curr_count)
#         coin_count += curr_count
#     if K == 0:
#         print(coin_count)
#         break


# 동전의 종류 개수, 목표 금액 입력
N, K = map(int, input().split())
# 동전의 가치를 저장할수있게 리스트로 초기화
coins = []
# 동전의 가치를 반복문으로 값 삽입
for _ in range(N):
    coins.append(int(input()))
# 동전의 가치 순서를 내림차순으로 변경
coins = coins[::-1]
# 동전 개수 최솟값
result = 0

# 내림차순으로 정렬한 동전들을 
# 목표금액 K를 0이 될때까지 가진 동전 종류로 나누어 최솟값구하기
for coin in coins:

    # 반복문 안에서 코인 개수 세기위한 초기화
    coin_count = 0

    # 내림차순으로 동전 개수 세기
    coin_count = K//coin   # ex) 4200 //  1000 =4 -> coin_count

    # 나눴을때 동전 개수가 1보다 크거나 같다면     
    if coin_count >= 1:

        # 목표금액을 현재금액 * 나눈 동전개수만큼 빼주기
        K -= coin*coin_count

        # 조건에 충족했을때 결과개숫값에 추가해주기
        result += coin_count
        
    # 목표금액이 0이되면 그동안 결과개숫값을 출력해주기
    if K == 0:
        print(result)
        break