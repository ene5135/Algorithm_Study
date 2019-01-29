import math

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