N = int(input())


for j in range(1, N+1):
    s = input()
    if ''.join(reversed(s.upper())) == s.upper():
        print("#{0} YES".format(j))
    else:
        print("#{0} NO".format(j))

