# 혼자 힘으로 푼 두번째 카카오 문제.... ㅎ

def solution(n, arr1, arr2):
    arr1_list = []
    arr2_list = []
    for a1 in arr1:
        value = bin(a1)
        v = value[2:]
        print(v)
        while len(v) < n:
            v = '0' + v
        arr1_list.append(v)
    print(arr1_list)
    for a2 in arr2:
        value = bin(a2)
        v = value[2:]
        while len(v) < n:
            v = '0' + v
        arr2_list.append(v)

    answer = [int(x)+int(y) for x,y in zip(arr1_list, arr2_list)]

    final = []
    for i in answer:
        # 이 예외처리 까다로웠음
        while len(str(i)) < n:
            i = '0' + str(i)
        tmp = str(i).replace("1", '#').replace("2", '#').replace('0', ' ')
        final.append(tmp)
    return final


print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))

