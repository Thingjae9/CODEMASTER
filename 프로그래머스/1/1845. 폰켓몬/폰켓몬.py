def solution(nums):
    answer = 0
    choice = int(len(nums)/2)
    pon = set(list(nums))
    if choice <= len(pon):
        answer = choice
    else:
        answer = len(pon)
    
    return answer