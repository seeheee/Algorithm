# 1. 일반 방식으로 풀기
def solution(new_id):
    new_ids = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    for i in new_id:
        if i in '.' or i in '_' or i in '-' or i.isalnum():
            new_ids += i

    # 3단계
    while '..' in new_ids:
        new_ids = new_ids.replace('..', '.')

    # 잘못된 4단계(이렇게 하게되면은 모든 .을 바꾼다)
    # len(new_ids) > 1가 없으면 두번째 if문에서 index error 발생
    # . 하나일 경우 첫번째 if문으로 제거되어서 문자열이 비었는데 또 if문을 돌려고 하니까는..
    if new_ids[0] == '.' and len(new_ids) > 1:
        new_ids = new_ids[1:]
    if new_ids[-1] == '.':
        new_ids = new_ids[:-1]

    if not new_ids:
        new_ids = 'a'

    if len(new_ids) >= 16:
        new_ids = new_ids[:15]
        if new_ids[-1] == '.':
            new_ids = new_ids[:-1]

    while len(new_ids) < 3:
        new_ids += new_ids[-1]

    return new_ids


# 2. 정규 표현식 사용
import re

def solution(new_id):

    # 1,2단계 완료
    new_ids = ''

    new_ids = re.sub('[^a-z\d\-\.\_]', '', new_id.lower())
    new_ids = re.sub('\.\.+', '.', new_ids)
    new_ids = re.sub('^\.|\.$', '', new_ids)

    if not new_ids:
        new_ids = 'a'

    new_ids = re.sub('\.$', '', new_ids[0:15])

    while len(new_ids) < 3:
        new_ids += new_ids[-1]

    return new_ids


print(solution("=.="))

# answer = 'ahsjkd'
# print(answer[0:15])