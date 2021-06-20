def solution(seoul):
    for s in seoul:
        if s in 'Kim':
            return "김서방은 " + str(seoul.index('Kim')) + "에 있다"

print(solution(["Jane", "Kim"]))