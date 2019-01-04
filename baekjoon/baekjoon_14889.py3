def get_score_diff(N, matrix, team):
    team0_score = 0
    team1_score = 0
    
    team0 = []
    team1 = []
    
    for idx, elt in enumerate(team):
        if elt == 0:
            team0.append(idx)
        else:
            team1.append(idx)
            
    for i in team0:
        for j in team0:
            if i==j:
                continue
            team0_score += matrix[i][j]
            
    for i in team1:
        for j in team1:
            if i==j:
                continue
            team1_score += matrix[i][j]
            
    
    
    """
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if team[i] == team[j]: # 같은팀
                if team[i] == 0: 
                    team0_score += matrix[i][j]
                else:
                    team1_score += matrix[i][j]
    """         
    return abs(team0_score - team1_score)

def get_max_combs(N, matrix, more, curr_idx, team):
    if more == 0 :
        return get_score_diff(N, matrix, team)
    
    result = 99999999
    
    for idx in range(curr_idx, N):
        team[idx] = 1
        result = min(result, get_max_combs(N, matrix, more-1, idx+1, team))
        team[idx] = 0
    
    return result
    

def solution(N, matrix):
    #print(N, matrix)

    result = get_max_combs(N, matrix, N/2, 0, [0]*N)
    
    return result
    
if __name__ == '__main__':
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    print(solution(N, matrix))
    