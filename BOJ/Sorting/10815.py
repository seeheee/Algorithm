N = int(input())

in1 = set(map(int, input().split()))

M = int(input())
in2 = list(map(int, input().split()))

result = []

# 이중 for문을 쓰면 시간초과가 난다 따라서 set(집합)의 in을 사용한다.
for i in in2:
    if i in in1:
        print(1, end=' ')
    else:
        print(0, end=' ')