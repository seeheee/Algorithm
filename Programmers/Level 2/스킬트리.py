def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        tmp = []  # 여기에 선언해야 skill_tree 불러올때마다 다시 tmp가 호출되면서 가능
        for sk in skill_tree:
            if sk in skill:
                tmp.append(sk)

        if skill.startswith(''.join(tmp)):
            answer += 1
    return answer