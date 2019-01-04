def solution(N, M, city):
    #print(N, M, city)
    customers = []
    stores = []
    for x in range(N):
        for y in range(N):
            if city[y][x] is 1:
                customers.append((x,y))
            elif city[y][x] is 2:
                stores.append((x,y))
    
    #print(customers, stores)
    result = 9999
    store_cases = choose_M(stores, M)
    
    for case in store_cases:
        case_dist_sum = 0
        for customer in customers:
            customer_dist_min = 9999
            for store in case:
                dist = abs(customer[0]-store[0])+abs(customer[1]-store[1])
                if dist < customer_dist_min:
                    customer_dist_min = dist
            case_dist_sum = case_dist_sum + customer_dist_min
        if case_dist_sum < result:
            result = case_dist_sum
            
    return result
            
    
def choose_M(stores, M):
    if M is 0:
        return [[]]
    if M >= len(stores):
        return [stores]
    
    result = []
    new_stores = stores.copy()
    for store in stores:
        del new_stores[0]
        for case in choose_M(new_stores, M-1):
            result.append([store]+case)
            
    return result
    
if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    city = [list(map(int, input().split())) for _ in range(N)]
    
    result = solution(N, M, city)
    print(result)
        
