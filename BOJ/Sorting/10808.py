in1 = input()

letters = 'abcdefghijklmnopqrstuvwxyz'
dic = {}

for i in letters:
    dic[i] = 0

for j in in1:
    dic[j] += 1

for k in dic.values():
    print(k, end=' ')

