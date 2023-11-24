from itertools import product

def solution(user_id, banned_id):
    candidates = []
    for banned in banned_id:
        candidate = []
        for user in user_id:
            if len(user) != len(banned):
                continue
            match = True
            for i in range(len(user)):
                if banned[i] == '*':
                    continue
                if banned[i] != user[i]:
                    match = False
                    break
            if match:
                candidate.append(user)
        candidates.append(candidate)

    combinations = set()
    for candidate in product(*candidates):
        if len(set(candidate)) == len(banned_id):
            combinations.add(tuple(sorted(candidate)))

    return len(combinations)