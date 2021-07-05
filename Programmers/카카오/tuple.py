# 20,111 이렇게 숫자로 안 되고 2,0,1,1,1 이렇게 카운트되는거 해결해야함

from collections import Counter

s = "{{20,111},{111}}"
list1 = []
for i in s:
    if i == '{' or i == '}' or i == ',':
        continue
    else:
        list1.append(int(i))

counter = Counter(list1)
print(counter)
answer = list(k for k in counter.keys())
print(answer)