import math
"""
더 이상적인 풀이는 min heap과 max heap을 각각 유지하는데 값으로 해당 노드의 인덱스 값도 가지도록 구현한다.
노드 삭제 시 삭제된 인덱스는 딕셔너리에 기록한다.
삭제시 우선 pop을 하고 pop한 노드의 인덱스가 딕셔너리에 기록되어있으면 이는 상대편 heap에서 이미 삭제된 노드라는 의미이므로 버리고 다시 pop을 한번 더 한다.
"""


def find_min_idx(l):
    minimum = math.inf
    result = -1
    for idx, val in enumerate(l):
        if minimum > val:
            minimum = val
            result = idx
    return result
        
def find_max_idx(l):
    maximum = -math.inf
    result = -1
    for idx, val in enumerate(l):
        if maximum < val:
            maximum = val
            result = idx
    return result

def solution(operations):
    inserted = []
    for op in operations:
        if op[0] == "I":
            inserted.append(int(op[2:]))
        else:
            if inserted == []:
                continue
            if op[2] == "-":
                del inserted[find_min_idx(inserted)]
            else:
                del inserted[find_max_idx(inserted)]
    
    if inserted == []:
        return [0,0]
    return [inserted[find_max_idx(inserted)], inserted[find_min_idx(inserted)]]
