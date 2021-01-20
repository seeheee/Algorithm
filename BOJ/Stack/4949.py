import sys
input = sys.stdin.readline


while True:
    # rstrip()을 사용하지 않을 시 .\n 이렇게 입력이 들어와서 break문을 나갈 수 없음
    str = input().rstrip()
    print(list(str))
    answer = []
    state = True
    if str == '.':
        break
    for i in str:
        if i == '(' or i == '[':
            answer.append(i)
        elif i == ']':
            if len(answer) == 0 or answer[-1] != '[':
                state = False
                break
            answer.pop()
        elif i == ')':
            if len(answer) == 0 or answer[-1] != '(':
                state = False
                break
            answer.pop()

    if len(answer) != 0:
        state = False
    if state:
        print('yes')
    else:
        print('no')


