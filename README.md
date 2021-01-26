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

```python

```

Counter
