from itertools import combinations
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
n_col = len(relation[0])
n_row = len(relation)
candidates=[]
for i in range(1,n_col+1):
    candidates.extend(combinations(range(n_col),i))

print(candidates)

final = []
for keys in candidates:
    tmp = [tuple([item[key] for key in keys]) for item in relation]
    print(tmp)
    if len(set(tmp)) == n_row:
        final.append(keys)
print(final)
        # print(final)

# 유일성 체크
final = []
for keys in candidates:
    tmp = []
    for r in relation:
        tmp.append(tuple([r[key] for key in keys]))

    if len(set(tmp)) == r:
        final.append(keys)
print(final)