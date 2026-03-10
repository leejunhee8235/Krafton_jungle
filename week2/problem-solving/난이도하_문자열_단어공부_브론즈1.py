# # 문자열 - 단어 공부 (백준 브론즈1)
# # 문제 링크: https://www.acmicpc.net/problem/1157
# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# alph = input().lower()

# for i in range(alph):
#     if alph[i] == alph[i+1]:
#         print("?")
#     else:
word = input().upper()
alphabet = list(set(word))

counte = []

for i in alphabet:# B A 
    counte.append(word.count(i))  # [1,3]

if counte.count(max(counte)) > 1: # counte.count(3)-> 1
    print("?")
else:
    print(alphabet[counte.index(max(counte))]) # alphabet[counte.index(3)] -> alphabet[1] -> A
    