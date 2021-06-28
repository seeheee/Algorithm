def solution(n):
    n_list = list(map(str, str(n)))
    n_list.sort(reverse=True)
    a = "".join(n_list)
    return int(a)

print(solution(118372))