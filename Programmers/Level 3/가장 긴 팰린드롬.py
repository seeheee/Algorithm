# i가 0일 경우, j는 1~8 즉 7까지
# i가 0 - 1, 0 - 2, 0-3, 0-4, 0-5, 0-6, 0-7
# i가 1인 경우, j는 2~7
# 1-2,1-3,1-4,1-5,1-6,1-7
# i가 2인 경우, j는 3~7
# 2-3,2-4,2-5,2-6,2-7
# i가 3인 경우, j는 4~7
# 3-4,3-5,3-6,3-7
# i가 4인 경우 j는 5~7
# 4-5,4-6,4-7
# i가 5인 경우 j는 6~7
# 5-6,5-7
# i가 6인 경우 j는 7
# 6-7

def ispalindrom(x):
    if x == x[::-1]:  # 원래 문자열과 뒤집은 문자열이 같은지 확인
        return True

def solution(s):
    MAX = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            print(s[i:j])
            if ispalindrom(s[i:j]):
                if MAX < len(s[i:j]):  # 가장 긴 팰린드롬을 찾기 위해서
                    MAX = len(s[i:j])
    return MAX

