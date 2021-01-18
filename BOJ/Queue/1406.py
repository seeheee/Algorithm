from collections import deque
import sys
input = sys.stdin.readline

init = list(input().strip())
left = deque(init)
right = deque()
N = int(input())

class Stack:
    def P(self, x):
        left.append(x)
    def L(self):
        if len(left) != 0:
            right.appendleft(left.pop())
    def D(self):
        if len(right) != 0:
            left.append(right.popleft())
    def B(self):
        if len(left) != 0:
            left.pop()


stack = Stack()
for i in range(N):
    order = input().strip().split(' ')
    if order[0] == 'P':
        stack.P(order[1])
    elif order[0] == 'L':
        stack.L()
    elif order[0] == 'D':
        stack.D()
    elif order[0] == 'B':
        stack.B()


result = left + right

for j in result:
    print(j, end='')