import math
def solution(brown, red):
    answer = []
    for i in range(1,int(math.sqrt(red))+1):
        if red % i == 0:
            horizon = int(red / i)
            vertical = i
            outline = horizon*2 + vertical*2 + 4
            if brown == outline:
                return [horizon+2, vertical+2]
    return answer