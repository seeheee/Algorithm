# 유니온 파인드 알고리즘 사용(union - find)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
parent = [i for i in range(N+1)]


# 부모 노드를 찾는 함수
def find(v):
    if v == parent[v]:
        return v

    parent[v] = find(parent[v]) # 트리의 높이를 "압축"
    return parent[v]


# 두 부모노드를 합치는 함수 (즉, 그래프 연결해서 더 작은 값으로 부모느드를 변경하는 함수)
def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(M):
    c, n1, n2 = map(int, input().split())
    if c == 0:
        union(n1, n2)
    else:
        if find(n1) == find(n2): #체크
            print("YES")
        else:
            print("NO")
