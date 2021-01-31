from collections import deque
TC = int(input())


card = []
que = deque()
for i in range(TC):
    N = int(input())
    in1 = input().split()
    card.append(in1)

    real = card[i]

    list_sort = sorted(real[1:])
    print("list_sort", list_sort)
    result = []
    # for j in range(0, len(list_sort)):
    result.append(list_sort[0: len(list_sort)//2])
    result.append(real[0])
    result.append(list_sort[len(list_sort)//2: ])
    print(result)


