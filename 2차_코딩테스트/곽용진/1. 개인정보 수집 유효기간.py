def solution(today, terms, privacies):
    answer = []
    ty, tm, td = today.split('.')
    ty, tm, td = int(ty), int(tm), int(td)
    terms_dict = dict()
    for i in range(len(terms)):
        term, m = terms[i].split()
        terms_dict[term] = int(m)
    
    for i in range(len(privacies)):
        day, t = privacies[i].split()
        
        y, m, d = day.split(".")
        y, m, d = int(y), int(m), int(d)
        
        m += terms_dict[t]
        d -= 1

        if d == 0:
            d = 28
            m -= 1

        if m > 12:
            y += (m//12)
            m %= 12
        
        if m == 0:
            m = 12
            y -= 1

        if ty > y:
            answer.append(i+1)
            continue
        elif ty < y:
            continue
        else: # y가 같으면
            if tm > m:
                answer.append(i+1)
                continue
            elif tm < m:
                continue
            else:
                if td > d:
                    answer.append(i+1)
                    continue
                elif td < d:
                    continue
        
    return answer   
