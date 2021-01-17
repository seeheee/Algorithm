str = list(input())
N = int(input())

print(str[-1])
print(str[-2])


class Stack:
    def __init__(self):
        self.pos = -1
    def P(self, x):
        str.append(x)
    def L(self):
        if len(str) - (2*len(str)) == -(len(str)):
            return self.pos
        else:
            return self.pos - 1
    def D(self):
        return self.pos+1
    def B(self):
        del str[-1]
        ++self.pos
# 이거 아무리봐도 너무 어려워
stack = Stack()
for i in range(N):
    order = input().split(' ')
    if order[0] == 'P':
        stack.P(order[1])
    elif order[0] == 'L':
        print(stack.L())
    elif order[0] == 'D':
        print(stack.D())
    elif order[0] == 'B':
        print(stack.B())

print(str)