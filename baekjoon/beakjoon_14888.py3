import math

def calculate(curr_res, A, ops):
  #  print(curr_res, A, ops)
    
    if A == []:
        return curr_res, curr_res

    max_res = -math.inf
    min_res = math.inf
    
    for idx, n_op in enumerate(ops):
        if n_op == 0:
            continue
        if idx == 0: # 덧셈
            new_res = curr_res + A[0]
        elif idx == 1: # 뺄셈
            new_res = curr_res - A[0]
        elif idx == 2: # 곱셈
            new_res = curr_res * A[0]
        elif idx == 3: # 나눗셈
            if curr_res < 0:
                new_res = (-curr_res) // A[0]
                new_res = -new_res
            else:
                new_res = curr_res // A[0]
            
        ops[idx] -= 1
        res = calculate(new_res, A[1:], ops)
        ops[idx] += 1 # back tracking
        
        max_res = max(max_res, res[0])
        min_res = min(min_res, res[1])
        
    return max_res, min_res
            
            

def solution(N, A, ops):
    #print(N, A, ops)
    result = calculate(A[0], A[1:], ops)
    
    return result
    
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    ops = list(map(int, input().split()))
    
    result = solution(N, A, ops)
    print(result[0])
    print(result[1])
    