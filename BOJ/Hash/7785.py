# 시간 초과 발생 (딕셔너리 안 썼음)
# find 함수는 효율성이 떨어짐
# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# log = []
# for i in range(N):
#     log.append(input().rstrip())
#
# log.sort(reverse=True)
#
# for i in log:
#     if 'leave' in i:
#         log.remove(i)
#     else:
#         if 'enter' in i:
#             print(i[:i.find(' ')])

import sys
input = sys.stdin.readline

N = int(input())

dic = {}

for _ in range(N):
    name, input_output = input().rstrip().split()
    if input_output == 'enter':
        dic[name] = True
    elif input_output == 'leave':
        del dic[name]


for i in sorted(dic.keys(), reverse=True):
    print(i)

# list 형태
print(sorted(dic.keys(), reverse=True))

# join함수는 리스트의 문자열들을 합치는 역할을 함 ( 공백을 사이에 두고 합쳐라 )
# print("\n".join(sorted(dic.keys(), reverse=True)))
