N = ['1','2','3','4','5','6','7','8','9']
def init_set(numbers, count):
    result = []
    if count == 0:
        return [""]
    for idx, num in enumerate(numbers):
        result += list(map(lambda x: num + x, init_set(numbers[0:idx]+numbers[idx+1:], count-1)))
    return result

def get_all_combs(ball_count):
    result = []
    if ball_count == "":
        return [""]
    for idx, char in enumerate(ball_count):
        result += list(map(lambda x: char + x, get_all_combs(ball_count[0:idx]+ball_count[idx+1:])))
    return list(set(result))

def get_case(number, strike, ball):
    SBA = 'S'*strike + 'B'*ball + 'A'*(3-(strike+ball))
    combs = get_all_combs(SBA)
    result = []
    for ball_count in combs:
        temp = [""]
        for i in range(3):
            if ball_count[i] == 'S':
                temp = [t+number[i] for t in temp]
            elif ball_count[i] == 'B':
                temp_temp = []
                for n in range(3):
                    if n != i and ball_count[n] != 'S':
                        temp_temp += [t+number[n] for t in temp]
                temp = temp_temp
            else:
                temp_temp = []
                for n in N:
                    if n in number:
                        continue
                    temp_temp += [t+n for t in temp]
                temp = temp_temp
        result += temp
        print(number, ball_count, temp)
    return set(result)
    
def solution(baseball):
    answer = 0
    result = set(init_set(N, 3))
    for cursor in baseball:
        result &= get_case(str(cursor[0]), cursor[1], cursor[2])
    return len(result)