# # 스택 - 스택 (백준 실버 4)
# # 문제 링크: https://www.acmicpc.net/problem/10828
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 
# 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.



# 1. 명령 개수 입력받기
M = int(input())

# 2. 스택으로 사용할 빈 리스트 만들기
stack = []
# 3. 출력값들을 저장할 리스트 만들기
save = []
# 4. 명령 개수만큼 반복
for _ in range(M):
    
    # 4-1. 한 줄 입력받기
    O = input()
    O = O.split()
    # 4-2. 만약 명령이 "push X" 형태라면
    if O[0] == "push":
        stack.append(int(O[1]))

    # 4-3. 만약 명령이 "pop" 이라면
    if O[0] == "pop":
       if not stack:
           save.append(-1)
       else:
           save.append(stack.pop())

    # 4-4. 만약 명령이 "size" 라면
    if O[0] == "size":
        save.append(len(stack))

    # 4-5. 만약 명령이 "empty" 라면
    if O[0] == "empty":
        if not stack:
           save.append(1)
        else:
           save.append(0)


    # 4-6. 만약 명령이 "top" 이라면
    if O[0] == "top":
        if not stack:
            save.append(-1)
        else:
            save.append(stack[-1])



# 5. 저장한 출력값들을 한 줄씩 출력
for i in save:
    print(i)