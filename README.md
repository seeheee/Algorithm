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
split() : 문자열을 구분자 기준에 따라 나누기<br>

https://appia.tistory.com/178<br>
isalpha() : 문자열이 알파벳인지 확인, 알파벳이면 True 아니면 False<br>
isdigit() : 문자열이 숫자인지 확인, 숫자이면 True 아니면 False<br>

### 💡 순열과 조합 그리고 중복 순열(combinations, permutations, product)
참고: https://velog.io/@insutance/Python-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC

조합을 사용하는 경우는 언제일까 ❓
1. 1,2,3의 숫자가 적힌 카드가 있을 때, 이 중 두 장을 꺼내는 경우의 수 -> 12,13,21,23,31,32
2. 'A', 'B', 'C'로 만들 수 있는 경우의 수 -> 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'

### 순열(permutations)
* 중복을 허용하지 않는다. 즉 11,22,33 나올 수 없음
* 순서에 의미가 있다. (= 같은 값이 뽑히더라도 순서가 다르면 다른 경우의 수로 판단)

```python
from itertools import permutations
pool = ['1', '5', '7']

print(list(map(''.join, permutations(pool, 2))))

# ['15', '17', '51', '57', '71', '75']
```

```python
from itertools import permutations

print(list(permutations([1,2,3,4], 2)))
print(list(permutations([1,2,3,1], 2)))

# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
# [(1, 2), (1, 3), (1, 1), (2, 1), (2, 3), (2, 1), (3, 1), (3, 2), (3, 1), (1, 1), (1, 2), (1, 3)]
```

## 중복 순열(product)

* 중복을 허용하는 순열 따라서 product는 두 개 이상의 리스트의 모든 조합을 구할 때 사용

```python
from itertools import product
pool =[(1, -1), (1, -1), (1, -1), (1, -1), (1, -1)]

print(list(map(sum, product(*pool))))
# [5, 3, 3, 1, 3, 1, 1, -1, 3, 1, 1, -1, 1, -1, -1, -3, 3, 1, 1, -1, 1, -1, -1, -3, 1, -1, -1, -3, -1, -3, -3, -5]
```

```python
from itertools import product

print(list(product([1,2,3,4], repeat=2)))
print(list(product([1,2,3,1], repeat=2)))

# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]
# [(1, 1), (1, 2), (1, 3), (1, 1), (2, 1), (2, 2), (2, 3), (2, 1), (3, 1), (3, 2), (3, 3), (3, 1), (1, 1), (1, 2), (1, 3), (1, 1)]
```

### 조합(combinations)
* 중복을 허용하지 않는다.
* 순서에 의미가 없다. (= 같은 값이 뽑히면 같은 경우의 수로 판단)

```python
from itertools import combinations

print(list(combinations([1,2,3,4], 2)))
print(list(combinations([1,2,3,1], 2)))

# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# [(1, 2), (1, 3), (1, 1), (2, 3), (2, 1), (3, 1)]
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

### 💡 map과 lambda, zip
https://digital-play.tistory.com/56<br>
https://www.daleseo.com/python-zip/

### 💡 split()랑 split(" ")의 차이
✌ 공백까지 리스트에 담기는 경우

```python
s = "try helllo world     try"
s_split = s.split(' ')
print(s_split)
# ['try', 'helllo', 'world', '', '', '', '', 'try']
```

✌ 구분자를 생략하는 경우

```python
s = "try helllo world     try"
s_split = s.split()
print(s_split)
# s_split = ['try', 'helllo', 'world', 'try']
```

### 💡 reverse와 reversed
✌ reverse는 **list타입에서 제공하는 함수**로써 반환값이 없다.

```python
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
d = {'a': 1, 'b': 2, 'c': 3}
s = 'abc'

l.reverse()  # ['c', 'b', 'a']
t.reverse()  # AttributeError: 'tuple' object has no attribute 'reverse'
d.reverse()  # AttributeError: 'dict' object has no attribute 'reverse'
s.reverse()  # AttributeError: 'str' object has no attribute 'reverse'
```

✌ reversed는 내장함수로, list에서 제공하는 함수가 아니고 **reversed는 ‘reversed’ 객체를 반환**한다.

```python
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
d = {'a': 1, 'b': 2, 'c': 3}
s = 'abc'

print(list(reversed(l)))  # ['c', 'b', 'a']
print(list(reversed(t)))  # ['c', 'b', 'a']
print(tuple(reversed(d)))  # ('c', 'b', 'a')
print(list(reversed(s)))  # ['c', 'b', 'a']
```

👀 dictionary는 키를 반대로 

```python
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
d = {'a': 1, 'b': 2, 'c': 3}
s = 'abc'

reversed(l)  # <listreverseiterator object at 0x101053c10>
reversed(t)  # <reversed at 0x1f23fec0790>
reversed(d)  # <dict_reversekeyiterator at 0x1f23fec1b80>
reversed(s)  # <reversed at 0x1f23fe6be20>
```


