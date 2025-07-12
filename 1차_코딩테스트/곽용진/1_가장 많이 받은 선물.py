def solution(friends, gifts):
    graph = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    gift_indi = [[0, 0, 0] for _ in range(len(friends))]
    chk = dict()
    for i in range(len(friends)): # muzi 넣으면 인덱스 반환
        chk[friends[i]] = i
        
    for i in range(len(gifts)):
        giver, receiver = gifts[i].split()
        graph[chk[giver]][chk[receiver]] += 1 # 준 사람, 받은 사람 표시
        gift_indi[chk[giver]][0] += 1
        gift_indi[chk[receiver]][1] += 1
    
    for i in range(len(gift_indi)):
        gift_indi[i][2] = gift_indi[i][0] - gift_indi[i][1]
        
    result = [0] * (len(friends))
    
    for i in range(len(graph)):
        gift_cnt = 0
        for j in range(len(graph)):
            if i == j:
                continue
            
            if graph[i][j] > graph[j][i]:
                gift_cnt += 1
            
            elif graph[i][j] == graph[j][i]:
                if gift_indi[i][2] > gift_indi[j][2]:
                    gift_cnt += 1
        result[i] = gift_cnt
    
    return max(result)
            
