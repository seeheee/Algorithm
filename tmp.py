a = ["119", "97674223", "1195524421"]
string_set = set(a)

dic = {}

list1 = []
for i in a:
    if dic[i] != i:
        list1.append(i)

print(list1)
