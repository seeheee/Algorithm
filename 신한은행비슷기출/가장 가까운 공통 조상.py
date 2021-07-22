from collections import deque, defaultdict

# LCA 알고리즘 사용(이거 다시 보기 - 관련문제 11437, 11438)
case = int(input())
for _ in range(case):
    N = int(input())
    parant = [0] * (N+1)
    for _ in range(N-1):
        p, c = map(int, input().split())
        parant[c] = p # 거슬러 올라가는 방식
    n1, n2 = map(int, input().split())

    n1_list = [n1]
    n2_list = [n2]

    while parant[n1]:
        n1_list.append(parant[n1])  # 부모 추가
        n1 = parant[n1]
    while parant[n2]:
        n2_list.append(parant[n2])
        n2 = parant[n2]   # 부모노드에서 또 위에 부모노드를 찾기 위해서

    n1_len = len(n1_list) - 1
    n2_len = len(n2_list) - 1

    while n2_list[n2_len] == n1_list[n1_len]: # 똑같은 부모노드가 있으면은 반복
        n2_len -= 1
        n1_len -= 1

    print(n1_list[n1_len+1])
