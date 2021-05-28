from collections import deque

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def bfs(begin, target, words, visited):
    count = 0
    que = deque()
    que.append(begin)
    while que:
        # popleft를 할 시 최소거리가 안 나옴, 모든 경우를 전부 따지기 때문
        # pop으로 할 시 2개 이상이 나올 경우 한 가지 경우만으로 따지고 한 가지 경우는 계속 que에 있어 안 써서 최소거리 가능
        start = que.pop()
        if target not in words:
            return 0
        if start == target:
            return count
        for i in range(len(words)):
            # 한 번에 한 개의 알파벳만 바꿀 수 있는 경우 생각 못함
            if len([j for j in range(len(words[i])) if words[i][j] != start[j]]) == 1:
                if visited[i] == 1:
                    continue
                visited[i] = 1
                que.append(words[i])
                print(que)
        count += 1
    return count

def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    answer = bfs(begin, target, words, visited)
    return answer

print(solution(begin,target,words))
