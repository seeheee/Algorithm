from itertools import combinations
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
n_col = len(relation[0])
n_row = len(relation)
candidates=[]
for i in range(1,n_col+1):
    candidates.extend(combinations(range(n_col),i))

# print(candidates)

# final = []
# for keys in candidates:
#     tmp = [tuple([item[key] for key in keys]) for item in relation]
#     # print(tmp)
#     if len(set(tmp)) == n_row:
#         final.append(keys)
# print(final)
        # print(final)

# 유일성 체크
final = []
for keys in candidates:
    tmp = []
    for r in relation:
        tmp.append(tuple([r[key] for key in keys]))

    if len(set(tmp)) == n_row:
        final.append(keys)
print("final", final)

answer = set(final)


for i in range(len(final)):
    for j in range(i+1, len(final)):
        if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
            print("element", final[j])
            answer.discard(final[j])
            print(answer)

# set()에서 특정 원소를 삭제하는 것은 2가지가 있음 (discard와 remove)
# discard는 remove와 다르게 지우려는 아이가 존재하지 않아도 에러가 발생하지 않는다.
if len(final[0]) == len(set(final[0]).intersection(set(final[1]))):
    answer.discard(final[1])
print(answer)