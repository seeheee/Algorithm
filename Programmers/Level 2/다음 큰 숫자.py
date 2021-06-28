def solution(n):
    num = n + 1
    while num <= 1000000:
        b = format(n, 'b')
        b1 = format(num, 'b')

        if b.count(str(1)) == b1.count(str(1)):
            print(b.count(str(1)))
            print(b1.count(str(1)))
            return num
        else:
            num += 1



# # 맨 처음 틀린 풀이(왜 틀린건지 모르겟음)
def solution(n):
    count = 0
    count2 = 0
    num = n + 1
    while num <= 1000000:
        b = format(n, 'b')
        b1 = format(num, 'b')

        for i in b:
            if int(i) == 1:
                count += 1
                # print(count)
        for j in b1:
            if int(j) == 1:
                count2 += 1
                # print(count2)

                if count == count2:
                    return num
                else:
                    num += 1



print(solution(15))