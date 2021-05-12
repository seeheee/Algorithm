# 62번 Unique Paths
# 뭔가 bfs 같은데 dp라서 신기
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        field = [[0]*m for _ in range(n)]
        direction = [(0,-1), (-1,0)]

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:  #오른쪽, 아래로만 움직이는 경우이므로 예외
                    field[i][j] = 1
                    continue

                for next in direction:
                    r, c = next
                    tmp_r = i + r
                    tmp_c = j + c
                    # 인덱스 범위가 0보다 작으면 안되고 (n,m)을 넘으면 다음으로 for문 반복
                    if tmp_c < 0 or tmp_r < 0 or n <= tmp_r or m <= tmp_c:
                        continue
                    field[i][j] += field[tmp_r][tmp_c]
        return field[n-1][m-1]