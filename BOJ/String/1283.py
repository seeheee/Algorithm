from collections import deque

N = int(input())

word = []
check = deque()
for _ in range(N):
    in1 = input().split()
    word.append(in1)
print("리스트", word)

count = 0
for i in word:
    for j in i:
        print("j", j)
        if j[0].capitalize() not in check:
            check.append(j[0].capitalize())
        else:
            for a in j.upper():
                if a not in check:
                    check.append(a)


# for i in word:
#     print(i[i.find(" ")+1:])
#     # 단어의 첫글자 check에 저장
#     if i[0].capitalize() not in check:
#         check.append(i[0].capitalize())
#     # 단어 중 공백이 있는 경우 공백 뒤의 앞글자 확인
#     elif i.find("") != -1 and i[i.find(" ")+1].capitalize() not in check:
#         check.append(i[i.find(" ")+1].capitalize())
print(check)