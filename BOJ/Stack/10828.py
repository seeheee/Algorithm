import sys

input = sys.stdin.readline

N = int(input())
stack = []

def push(x):
    stack.append(x)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())


def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

for i in range(N):
    order = input()
    str = order.strip().split(' ')
    if str[0] == 'push':
        push(int(str[1]))
    elif str[0] == 'top':
        top()
    elif str[0] == 'pop':
        pop()
    elif str[0] == 'size':
        size()
    elif str[0] == 'empty':
        empty()
