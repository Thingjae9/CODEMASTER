def solution(numbers, hand):
    answer = ''
    # 왼손과 오른손의 시작 위치
    left, right = '*', '#'
    # 각 숫자별 위치
    positions = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    # 각 숫자별 왼손과 오른손 거리
    left_distance = {1: 0, 4: 0, 7: 0, '*': 0, 2: 1, 5: 1, 8: 1, 0: 1, 3: 2, 6: 2, 9: 2, '#': 3}
    right_distance = {3: 0, 6: 0, 9: 0, '#': 0, 2: 1, 5: 1, 8: 1, 0: 1, 1: 2, 4: 2, 7: 2, '*': 3}
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left = num
        elif num in [3, 6, 9]:
            answer += 'R'
            right = num
        else:
            # 왼손과 오른손의 거리 계산
            left_dist = abs(positions[num][0] - positions[left][0]) + abs(positions[num][1] - positions[left][1])
            right_dist = abs(positions[num][0] - positions[right][0]) + abs(positions[num][1] - positions[right][1])
            if left_dist < right_dist or (left_dist == right_dist and hand == 'left'):
                answer += 'L'
                left = num
            elif left_dist > right_dist or (left_dist == right_dist and hand == 'right'):
                answer += 'R'
                right = num
    return answer