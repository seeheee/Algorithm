import re

N = input()

numbers = re.findall("\d", N)

result = int(''.join(numbers))

print(result)

count = 0
for i in range(1, result+1):
    if result % i == 0:
        count += 1
print(count)


