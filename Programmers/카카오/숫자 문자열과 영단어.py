# dictionary와 replace가 생각났어야 했는데 둘 다 생각 안 났음
# 모두다 숫자일 경우 모두 다 돌면서 그냥 나옴
# 무언가 짝이 이뤄져 있는 표가 나올 경우 dictionary를 생각했어야 함...

# replace에 해당되는게 없다고 에러 나오지 않아
s = 'sksk'
s.replace("a", "0")
print(s)

def solution(s):
    sring_dic = {"zero": "0", "one": "1", "two": "2", "three": "3",
                 "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for k, v in sring_dic.items():
        s = s.replace(k, v)

    return int(s)

print(solution("one4seveneight"	))

# for문에서의 s를 찍어보면은...
# one4seveneight
# 14seveneight
# 14seveneight
# 14seveneight
# 14seveneight
# 14seveneight
# 14seveneight
# 147eight
# 1478
# 1478
# 1478