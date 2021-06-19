# Python Algorithm

#### 👀 문자열 메소드

len() : 문자열 길이<br>
min() : 문자열 혹은 숫자 최소값 (문자열일 경우 - 알파벳 순서, 숫자일 경우 - 숫자순서)<br>
max() : 문자열 혹은 숫자 최대값<br>
count() : 문자열안에서 매개변수로 입력한 문자열의 개수 세기

```python

a = 'I Love Python'

a.count('o', 7, len(a)) # count(string, begin, end)
```

find() : 문자열에 매개변수로 입력한 문자열을 앞에서부터 찾아 index 반환, 없으면 -1 반환<br>
rfind() : 문자열 뒤에서부터 찾아 index 변환, 없으면 -1 반환<br>
index(), rindex() : 각각 find, rfind와 동일, 없으면 에러 발생<br>

lower() : 문자열 내 모든 문자 소문자로 변환<br>
upper() : 문자열 내 모든 문자 대문자로 변환<br>

lstrip() : 문자열의 왼쪽에 있는 공백을 제거<br>
rstrip() : 문자열의 오른쪽에 있는 공백을 제거<br>
strip() : 문자열의 양쪽에 있는 공백을 제거<br>
  
split() : 문자열을 구분자 기준에 따라 나누기

### 💡 순열과 조합 그리고 카티션 곱(combinations, permutations, product)
조합을 사용하는 경우는 언제일까 ❓
1. 1,2,3의 숫자가 적힌 카드가 있을 때, 이 중 두 장을 꺼내는 경우의 수 -> 12,13,21,23,31,32
2. 'A', 'B', 'C'로 만들 수 있는 경우의 수 -> 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

```python
from itertools import permutations
pool = ['1', '5', '7']

print(list(map(''.join, permutations(pool, 2))))
```

product는 두 개 이상의 리스트의 모든 조합을 구할 때 사용

```python
from itertools import product
pool =[(1, -1), (1, -1), (1, -1), (1, -1), (1, -1)]

print(list(map(sum, product(*pool))))
# [5, 3, 3, 1, 3, 1, 1, -1, 3, 1, 1, -1, 1, -1, -1, -3, 3, 1, 1, -1, 1, -1, -1, -3, 1, -1, -1, -3, -1, -3, -3, -5]
```

## 💡 BFS/DFS 3가지 패턴

### 1️⃣ 상, 하, 좌, 우 패턴
```python
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
```

### 2️⃣ 대각선 + 상, 하, 좌, 우 패턴
```python
dx = [1, 0, -1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]
```

### 2️⃣ 대각선 패턴
```python
dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]
```

### 💡 list.count()
리스트에서 특정 원소가 몇번 등장하는지 결과를 정수 값으로 출력

1. 문자열 셈하기
```python
a = ['blue', 'blue', 'red', 'orange', 'green']
a.count('blue')
# 2
```
2. 숫자 셈하기
```python
b = [4, 1, 2, 2, 8, 1, 2]
b.count(2)
# 3
```

### 💡 2차원 리스트에서 최대값과 최소값 구하기
참고: https://devbull.xyz/python-2caweon-baeyeolyi-coedaegabs-coesogabs-cajgi/

#### 최대값 구하기
```python
max(map(max, list)
```

#### 최소값 구하기
```python
min(map(min, list)
```
