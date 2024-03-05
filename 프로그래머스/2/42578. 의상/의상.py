def solution(clothes):
    answer = 0
    hash = {}
    for cloth, type in clothes:
        hash[type] = hash.get(type, 0) + 1
    answer = 1
    for type in hash:
        answer *= (hash[type] + 1)
    answer -= 1           
    return answer