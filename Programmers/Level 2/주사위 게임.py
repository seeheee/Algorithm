
def solution(monster, S1, S2, S3):
    cand = []

    for i in range(1, S1 + 1):
        for j in range(1, S2 + 1):
            for k in range(1, S3 + 1):
                print(i, j, k)
                cand.append(i + j + k)

    count = 0
    for c in cand:
        if c + 1 not in monster:
            count += 1

    return int((count / len(cand)) * 1000)


# i,j,k
# 1 1 1
# 1 1 2
# 1 1 3
# 1 1 4
# 1 2 1
# 1 2 2
# 1 2 3
# 1 2 4
# 1 3 1
# 1 3 2
# 1 3 3
# 1 3 4
# 2 1 1
# 2 1 2
# 2 1 3
# 2 1 4
# 2 2 1
# 2 2 2
# 2 2 3
# 2 2 4
# 2 3 1
# 2 3 2
# 2 3 3
# 2 3 4


# # 주사위의 수가 2,3,4 인데 1,4,2와 1,4,1 같은 숫자도 뽑힘
# from itertools import permutations
#
# def solution(monster, S1, S2, S3):
#     cand = []
#     cand.extend(range(1, S1 + 1))
#     cand.extend(range(1, S2 + 1))
#     cand.extend(range(1, S3 + 1))
#
#     result = list(permutations(cand, 3))
#     print(result)
#
#     count = 0
#     for r in result:
#         _sum = sum(r)
#         if _sum + 1 not in monster:
#             count += 1
#
#     return int((count / len(result)) * 1000)