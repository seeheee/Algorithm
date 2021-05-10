# 네트워크

def solution(n, computers):
    answer = 0
    # 방문 안함(False), 방문함(True)
    computer_visited = [False for _ in range(n)]
    for i in range(n):
        if computer_visited[i] == False:
            bfs(n, i, computers, computer_visited)
            answer += 1 # bfs함수를 돈 횟수만큼 answer 출력
    return answer

def bfs(n, i, computers, computer_visited):
    computer_visited[i] = True # 방문했다는 표시
    que = []
    que.append(i) # 0번째부터 시작
    while que:
        node = que.pop(0) 
        computer_visited[node] = True # que가 있을 경우 그 node도 방문했다는 표시 필요
        for j in range(n):
            if node != j and computers[node][j] == 1:
                if computer_visited[j] == False:
                    que.append(j)