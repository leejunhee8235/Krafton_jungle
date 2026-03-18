# # 분할정복 - 곱셈 (백준 실버1)
# # 문제 링크: https://www.acmicpc.net/problem/1629
# 문제
# 자연수 A를 B번 곱한 수를 알고 싶다. 
# 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. 
# A, B, C는 모두 2,147,483,647 이하의 자연수이다.

# 출력
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
# import sys
# input = sys.stdin.readline

# M = list(map(int,input().split()))

# for i in range(M):
#     n[]

import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

def power(a, b, c):
    if b == 1:
        return a % c

    temp = power(a, b // 2, c)

    if b % 2 == 0:
        return (temp * temp) % c     # (a, 2, c),(a, 4, c)
    else:
        return (temp * temp * a) % c # (a, 1, c),(a, 3, c)

    
print(power(A, B, C))

# 지수가 1이면 a의지수 1이기에 a%C를 구하는걸로 리턴
# temp에 a의 절반 지수 제곱값을 구해서 저장
# 만약 지수가 짝수라면 (a지수b//2%c)  ex) a%

