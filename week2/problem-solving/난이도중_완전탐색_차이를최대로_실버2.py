# # 완전탐색 - 차이를 최대로 (백준 실버2)
# # 문제 링크: 
# 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

# n개의정수 배열a 

# TEST_CASE = int(input())   
# nums = list(map(int,input().split())) 
# # abs() (n-2)s - (n-1)
# for i in range(nums):
#         # base case 
#         if  

#         # 선택

#         # 탐색

#         # 취소



#         pass



# 백트랙 함수 (k,r,total)
#     베이스케이스
#         
#         if리멤버의 길이가 n일때 
#         총합 최댓값 구하기
#         return   
#         반복문 시작 i = 0
#         조건문 if i not in remember
#               remember.append(i)
#               backtrack( ,r[i],)
#               remember.pop()


n = int(input())
arr = list(map(int, input().split()))

remember = []
answer = 0

def backtrack():

    global answer

    # 베이스 케이스
    if len(remember) == n:

        total = 0
        for i in range(n-1):
            total += abs(remember[i] - remember[i+1])

        answer = max(answer, total)
        return

    # 반복문
    for i in range(n):

        if arr[i] not in remember:

            remember.append(arr[i])

            backtrack()

            remember.pop()


backtrack()
print(answer)