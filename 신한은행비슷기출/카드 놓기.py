from itertools import permutations

N = int(input())
c = int(input())
card = list(input() for _ in range(N))

permutation = set(map(''.join, permutations(card, c)))

result = []
for i in permutation:
    result.append(int(i))

print(len(result))