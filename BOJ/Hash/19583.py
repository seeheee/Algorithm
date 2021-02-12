import sys
start, end, streaming = map(str, input().split())
start = int("".join(start.split(':')))
end = int("".join(end.split(':')))
streaming = int("".join(streaming.split(':')))

dic = {}

while(True):
    line = sys.stdin.readline
    if len(line) < 5:
        break
    time, name = map(str, line.split())

