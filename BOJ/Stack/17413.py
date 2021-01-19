import sys

class Stack:
    def __init__(self):
        self.container = []
        self.count = 0

    def push(self, value):
        self.container.append(value)
        self.count += 1

    def pop(self):
        if self.empty() == 1:
            return -1
        self.count -= 1
        return self.container.pop()

# 1이면 True, 0이면 False
    def empty(self):
        if self.count == 0:
            return 1
        return 0


input = sys.stdin.readline().rstrip()


stack = Stack()
tag = False
result = ''

for i in input:
    if i == '<':
        while not stack.empty():
            result += stack.pop()
        result += i
        tag = True
    elif i == '>':
        result += i
        tag = False
    elif tag:
        result += i
    elif i == ' ':
        while not stack.empty():
            result += stack.pop()
        result += i
    else:
        stack.push(i)


# 아예 태그가 없는 경우 해당(push 한거 전부 빼기)
while not stack.empty():
    result += stack.pop()
print(result)

