import heapq
import collections
# 사전식순서를 유지하는 것을 찾아내는 것이 중요
# set함수를 sorted를 이용할 수 있다. -> 반환값이 리스트

# 재귀를 이용한 방법
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            char_slice = s[s.index(char):]
            if set(s) == set(char_slice):
                return char + self.removeDuplicateLetters(char_slice.replace(char, ''))
        # 맨 마지막 함수 재귀값에서 돌아오는 것이 필요해서 필요함
        return ''

# 스택을 이용한 방법
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = collections.Counter(s)
        for char in s:
            counter[char] -= 1
            # 중복되는 문자 제거(해당문자열 넘어감)
            if char in stack:
                continue
            # stack에 사전순으로 쌓이면서 또 나올 문자인지 확인
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            # 해당문자 넣기
            stack.append(char)

        return ''.join(stack)


if __name__ == '__main__':
    print(Solution().removeDuplicateLetters("cbacdcbc"))