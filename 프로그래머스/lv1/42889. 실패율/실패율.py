def solution(N, stages):
    answer = {}
    total = len(stages)

    for i in range(1, N+1, 1):
        member = stages.count(i)
        if member != 0:
            answer[i] = member / total
        else:
            answer[i] = 0
        total = total - member



    final = sorted(answer, key=answer.get, reverse=True)
    return final