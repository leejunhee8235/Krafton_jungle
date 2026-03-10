# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978
# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.
from math import sqrt
TEST_CASE = int(input())   # 4
nums = list(map(int,input().split())) # [1,3,5,7]

def sosu(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3,int(sqrt(num))+1,2):
        if num % i == 0:
            return False
    return True
       
       
result = []       
for i in range(TEST_CASE): # 1 3 5 7
     if sosu(nums[i]) == True:
           
           result.append(nums[i]) 
              
print(len(result))        
    

    

        

        
