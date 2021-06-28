# if문 생각 못 했음 멍청이임...
import math


def solution(n):
    nsqrt = math.sqrt(n)
    if nsqrt == int(nsqrt):
        return (nsqrt + 1) ** 2
    else:
        return -1
