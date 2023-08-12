def solution(n, arr1, arr2):
    answer = []
    for num in arr1:
        tmp = format(num, 'b')
        if len(tmp) == n:
            answer.append(int(tmp))
        else:
            while len(tmp) < n:
                tmp = '0'+tmp
            answer.append(int(tmp))
    
    for num in arr2:
        tmp = format(num, 'b')
        if len(tmp) == n:
            answer.append(int(tmp))
        else:
            while len(tmp) < n:
                tmp = '0'+tmp
            answer.append(int(tmp))
    
    check = []        
    for a in range(n):
        tmp = str(answer[a] + answer[a+n])
        if len(tmp) == n:
            check.append(tmp)
        else:
            while len(tmp) < n:
                tmp = '0'+tmp
            check.append(tmp)
    
    answer = []    
    for b in check:
        b = b.replace('1', '#')
        b = b.replace('2', '#')
        b = b.replace('0', ' ')
        answer.append(b)
        
    return answer