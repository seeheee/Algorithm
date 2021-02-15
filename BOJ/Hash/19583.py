import sys
start, end, streaming = map(str, input().split())
start = int("".join(start.split(':')))
end = int("".join(end.split(':')))
streaming = int("".join(streaming.split(':')))

dic = {}
count = 0
while(True):
    # 얼만큼 입력으로 들어올지 모르니까는 반복문을 돌면서 readline으로 받다가 길이가 짧으면 탈출
    line = sys.stdin.readline()
    if len(line) < 5:
        break
    time, name = map(str, line.split())
    time = int("".join(time.split(':')))
    if start >= time:
        dic[name] = 1
    elif end <= time <= streaming:
        # 중복된 데이터가 들어와도 한번만 카운트를 하기 위해서 if문에 값이 1일 경우를 넣어줌
        if dic.get(name) == 1:
            dic[name] += 1
            count += 1

print(count)


