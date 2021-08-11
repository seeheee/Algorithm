def solution(seat):
    visited = set()
    answer = 0

    for x, y in seat:
        if visited and (x, y) in visited:
            continue
        else:
            visited.add((x, y))
            answer += 1
    return answer