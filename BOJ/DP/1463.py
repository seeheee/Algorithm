# 다이나믹 알고리즘 푸는 방법
# 1. 테이블 정의하기
# 2. 점화식 찾기
# 3. 초기값 정의하기

in1 = int(input())

D = [0 for _ in range(1000001)]

# 리스트의 인덱스를 /(나누기)를 사용할 시 자동으로 float형이 되어버림
# 따라서 //을 사용하면 묵시적으로 int형으로 바꿔준다.


for i in range(2, in1+1):
    print(i)
    D[i] = D[i-1] + 1
    if i % 3 == 0:
        D[i] = min(D[i//3]+1, D[i])
    if i % 2 == 0:
        D[i] = min(D[i//2]+1, D[i])

print(D[in1])