S = input()

# 왼쪽에서부터 더하기 곱하기를 수행하니까는 기준점
result = int(S[0])

for i in range(1, len(S)):
    num = int(S[i])
    if num <= 1 or result <=1:
        result += num
    else:
        result *= num

print(result)
