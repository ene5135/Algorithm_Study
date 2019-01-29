def solution(participant, completion):
    parti_dict = {}
    for parti in participant:
        parti_dict[parti] = parti_dict.get(parti, 0) + 1
    for comp in completion:
        if parti_dict[comp] == 1:
            del parti_dict[comp]
        else:
            parti_dict[comp] = parti_dict[comp] - 1
    answer = list(parti_dict.keys())[0]
    return answer