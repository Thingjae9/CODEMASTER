def solution(participant, completion):
    hash = {} 
    for part in participant:
        if part in hash:
            hash[part] += 1 
        else:
            hash[part] = 1 
    for comp in completion:
        if hash[comp] == 1:
            del hash[comp]
        else:
            hash[comp] -= 1
    answer = list(hash.keys())[0] 
    return answer