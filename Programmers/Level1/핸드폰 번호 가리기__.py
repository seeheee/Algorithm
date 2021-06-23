def solution(phone_number):
    var = '*' * len(phone_number[:-4]) + phone_number[-4:]
    return var


print(solution("01033334444"))