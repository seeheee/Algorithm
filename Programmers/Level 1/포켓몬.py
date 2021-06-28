from itertools import permutations

nums = [3, 3, 3, 2, 2, 2]

def solution(nums):
    pokect = len(nums) // 2
    num = set(nums)
    return min(len(num), pokect)


print(solution(nums))