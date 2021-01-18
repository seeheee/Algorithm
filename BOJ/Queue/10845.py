from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

result = deque()

class Que:
    def push(self, x):
        result.append(x)
    def pop(self):
        if len(result) == 0:
            print(-1)
        else:
            print(result.popleft())
    def size(self):
        print(len(result))
    def empty(self):
        if len(result) == 0:
            print(1)
        else:
            print(0)
    def front(self):
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])
    def back(self):
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])



que = Que()
for i in range(N):
    order = input().strip().split(' ')
    if order[0] == 'push':
        que.push(order[1])
    elif order[0] == 'pop':
        que.pop()
    elif order[0] == 'empty':
        que.empty()
    elif order[0] == 'size':
        que.size()
    elif order[0] == 'front':
        que.front()
    elif order[0] == 'back':
        que.back()


