a = [1,2,3,4,5]
b = [2,1,2,3,2,4,2,5]
c = [3,3,1,1,2,2,4,4,5,5]
def solution(answers):
    result = []
    score_a, score_b, score_c = 0,0,0
    for idx, answer in enumerate(answers):
        if a[idx%5] == answer: 
            score_a += 1
        if b[idx%8] == answer:
            score_b += 1
        if c[idx%10] == answer:
            score_c += 1
    maximum = max([score_a, score_b, score_c])
    for idx, score in enumerate([score_a, score_b, score_c]):
        if score == maximum:
            result.append(idx+1)
    
    return result