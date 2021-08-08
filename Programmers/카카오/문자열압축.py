# stack 이용한 풀이
def solution(s):
    length = len(s)
    cand = [length]

    for size in range(1, length):
        compressed = ""
        splited = [s[i:i+size] for i in range(0, length, size)]
        stack = [[splited[0], 1]]

        print(stack)

        for sw in splited[1:]:
            if stack[-1][0] != sw:
                stack.append([sw, 1])
            else:
                stack[-1][1] += 1

        compressed += ''.join([str(cnt) + w if cnt > 1 else w for w, cnt in stack])

        cand.append(len(compressed))

    return min(cand)

# # count 지역변수 사용
# def solution(s):
#     length = len(s)
#     cand = [length]
#
#     for size in range(1, length):
#         compressed = ""
#         splited = [s[i:i+size] for i in range(0, length, size)]
#         count = 1
#
#         for sw in range(len(splited)-1):
#             if splited[sw] == splited[sw+1]:
#                 count += 1
#             else:
#                 if count > 1:
#                     compressed += str(count) + splited[sw]
#                 else:
#                     compressed += splited[sw]
#                 count = 1
#
#         if count > 1:
#             compressed += str(count) + splited[-1]
#         else:
#             compressed += splited[-1]
#         cand.append(len(compressed))
#
#     return min(cand)



# # 2개짜리인 경우 밖에 못함...
# def solution(s):
#     stack = []
#     answer = 0
#     for i in s:
#         stack.append(i)
#         if stack[-1] == i:
#             stack.pop()
#             answer += 1
#
#     return answer


print(solution("aabbaccc"))