def solution(phone_book):
    answer = True
    phone_dict = {}
    for phone in phone_book:
        phone_dict[phone] = phone
        
    for phone in phone_book:
        for i in range(len(phone)):
            sub = phone[0:i+1]
            if phone_dict.get(sub, False) and sub != phone:
                return False
                
    return True