# # 배열 - 평균은 넘겠지 (백준 브론즈1)
# # 문제 링크: https://www.acmicpc.net/problem/4344
# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다. 정답과 출력값의 절대/상대 오차는 10-3이하이면 정답이다.
# TEST_CASE = int(input())   # 5
# data = list(map(int,input().split())) # 5 50 50 70 80 100
# students = data[0]
# points = data[1:]
# count = 0
# percent = 0

# avg = sum(points)/students
# # 반 모든 학생의 총점과 평균
# for i in range(students):
#     # presult += points[i]
#     # paverage = presult/students
#     if points[i] > avg:
#         count+=1
# # 평균이상인 학생 수를 구하여 퍼센트화 .3f
# percent = (count/students)*100

    

# print(f"{percent:.3f}%")
    
TEST_CASE = int(input())

for _ in range(TEST_CASE):

    data = list(map(int, input().split()))
    
    students = data[0]
    points = data[1:]
    
    count = 0
    
    avg = sum(points) / students

    for i in range(students):
        if points[i] > avg:
            count += 1

    percent = (count / students) * 100

    print(f"{percent:.3f}%")
# 평균을 퍼센트로 구하는 식 = 학생 총 점수/ 학생 총 수     2239 / 32
# def pav(point):
#     if point < 0:
#         return False
#     if point > 100:
#         return False
#     for i in range(students):
#         result += pav(points[i])

#     return result
# def pstu(student):
#     if student == 0:
#         return 0
#     if student < 0:
#         return False
#     if student > 1000:
#         return False
#     if TEST_CASE > len(students):
#         return False
#     if TEST_CASE < len(students):
#         return False
#     for i in range(TEST_CASE):
       
#         else:
    
# print(pav(points))
    


