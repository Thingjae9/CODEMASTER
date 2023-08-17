def solution(dartResult):
    import re
    answer = 0
    result = re.findall('\d+[SDT][*#]?', dartResult)
    total = []
    for i in range(3):
        if len(result[i]) == 2:
            score = int(result[i][0])
            bonus = int(result[i][1].replace('S', '1').replace('D', '2').replace('T', '3'))
            total.append(score**bonus)
        elif len(result[i]) == 3:
            if result[i][0:2] == '10':
                score = 10
                bonus = int(result[i][2].replace('S', '1').replace('D', '2').replace('T', '3'))
                total.append(score**bonus)

            else:
                score = int(result[i][0])
                bonus = int(result[i][1].replace('S', '1').replace('D', '2').replace('T', '3'))
                award = int(result[i][2].replace('*', '2').replace('#', '-1'))
                if result[i][2] == '*':
                    if i == 0:
                        total.append(score**bonus*award)
                    else:
                        total[i-1] = total[i-1]*2
                        total.append(score**bonus*award)
                else:
                    total.append(score**bonus*award)

        elif len(result[i]) == 4:
            score = 10
            bonus = int(result[i][2].replace('S', '1').replace('D', '2').replace('T', '3'))
            award = int(result[i][3].replace('*', '2').replace('#', '-1'))
            if result[i][2] == '*':
                if i == 0:
                    total.append(score**bonus*award)
                else:
                    total[i-1] = total[i-1]*2
                    total.append(score**bonus*award)
            else:
                total.append(score**bonus*award) 
    return sum(total)