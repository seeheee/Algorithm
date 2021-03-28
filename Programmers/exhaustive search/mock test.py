# 모의고사
# 딕서녀리의 키값이 이미 정렬되어 있기에 정렬해 줄 필요 없음
# elif와 if 정확히 쓰기

def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    student1_cnt = 0
    student2_cnt = 0
    student3_cnt = 0

    list1 = []
    for idx, i in enumerate(answers):
        if i == student1[idx % 5]:
            student1_cnt += 1
        if i == student2[idx % 8]:
            student2_cnt += 1
        if i == student3[idx % 10]:
            student3_cnt += 1

    dic = {1: student1_cnt, 2: student2_cnt, 3: student3_cnt}
    highscore = max(dic.values())

    for key, val in dic.items():
        if val == highscore:
            list1.append(key)

    return list1
