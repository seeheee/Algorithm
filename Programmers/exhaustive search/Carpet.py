# 카펫
# 가로 세로 구하는 공식을 생각해내는 것이 어려움 ㅠㅠ

def solution(brown, yellow):
    a = 3
    while True:
        b = (yellow/(a-2)) + 2
        if b == int(b):
            b = int(b)
            if (a+b-2)*2 == brown:
                if a < b:
                    a,b = b,a
                return [a,b]
        a += 1