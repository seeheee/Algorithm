
while True:
    num = input()
    if num == '*':
        break
    for i in range(len(num) - 1):
        check = []
        state = False
        for j in range(len(num)-1-i):
                t = [num[j],num[j+i+1]]
                # print(t)
                if t in check:
                    state = True
                    print("{} is NOT surprising.".format(num))
                    break
                else:
                    # print("state", state)
                    check.append(t)
        if state:
            # print("여기", state)
            break
    else:
        print("{} is surprising.".format(num))





