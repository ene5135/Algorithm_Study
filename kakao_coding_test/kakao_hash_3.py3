def solution(clothes):
    cloth_dict = {}
    for cloth in clothes:
        cloth_dict[cloth[1]] = cloth_dict.get(cloth[1], []) + [cloth[0]]
        
    answer = 0
    values = list(cloth_dict.values())
    
    """
    bit map 이용 방법(2**30 case에 시간초과)
    
    for t in range(2**len(values)):
        bit_map = "0"*(len(values)-len(bin(t))+2) + bin(t)[2:]
        temp_answer = 1
        for i in range(len(values)):
            if bit_map[i] == "1":
                temp_answer *= len(values[i])
        answer += temp_answer
    """
    answer = 1
    for value in values:
        answer *= len(value)+1 # "안입는다" 를 의상으로 포함
        
    return answer-1