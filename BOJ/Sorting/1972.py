num = input()

while not num == '*':
    num = input()
    for i in range(len(num) - 1):
        for j in range(1, len(num)):
            if i+j >= len(num):
                break
            else:
                print(num[i],num[i+j])




