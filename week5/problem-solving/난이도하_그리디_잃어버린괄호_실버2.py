# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541
# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 
# 그리고 나서 세준이는 괄호를 모두 지웠다.

# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 
# 가장 처음과 마지막 문자는 숫자이다. 
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 
# 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 
# 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# 출력
# 첫째 줄에 정답을 출력한다.

# 한 줄 문자열 입력(식 전체)
# expr = input()              # 55-50+40
# # - 기준으로 자르기
# parts = expr.split('-')     # 55, 50+40

# result = 0                  # result 초기화
# for i in range(len(parts)): # parts(55, 50+40)의 길이만큼 반복
#     part = parts[i]         # i = 0 part에 55삽입  i = 1 part에 50+40 삽입
#     nums = part.split('+')  # i = 0 nums에 55삽입  i = 1 nums에 50 삽입 40 삽입

#     temp = 0                # 정수로 변환 뒷부분 묶음 합
#     for num in nums:        # i = 0 nums에 있는 55  i = 1 nums에 있는 50, 40
#         temp += int(num)    # i = 0 temp = temp+55

#     if  i == 0: 
#         result += temp      # result = result+temp
#     else:
#         result -= temp      # result = result-temp


sick = input()

parts = sick.split('-')

result  = 0
for i in range(len(parts)):
    part = parts[i]
    nums = part.split('+')

    temp = 0
    for num in nums:
        temp += int(num)

    if i == 0:
        result += temp
    else:
        result -= temp