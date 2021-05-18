import heapq
s = "cbacdcbc"

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remove = set()
        heap = []
        list2 = []

        for i in s:
            remove.add(i)

        for i in remove:
            heap.append(i)

        heapq.heapify(heap)

        while heap:
            result = heapq.heappop(heap)
            list2.append(result)

        answer = "".join(list2)
        return answer


if __name__ == '__main__':
    print(Solution().removeDuplicateLetters("cbacdcbc"))