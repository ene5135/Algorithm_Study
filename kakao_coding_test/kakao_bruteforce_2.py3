import math

def check_prime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True
def get_all_comb(numbers):
    result = []
    if numbers == "":
        return [""]
    for idx, number in enumerate(numbers):
        result += list(map(lambda x: number + x, get_all_comb(numbers[0:idx]+numbers[idx+1:])))
        result += get_all_comb(numbers[0:idx]+numbers[idx+1:])
    return result

def solution(numbers):
    combs = set([int(number) for number in get_all_comb(numbers) if number != '' and int(number) != 1 and int(number) != 0])
    answer = 0
    print(combs)
    for number in combs:
        if check_prime(number):
            answer += 1
    return answer