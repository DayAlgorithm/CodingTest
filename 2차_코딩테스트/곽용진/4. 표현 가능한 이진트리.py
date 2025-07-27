def chk(bits, start, end):
    if len(bits) == 0:
        return True
    mid = len(bits)//2
    if bits[mid] == '0': # 중앙이 0이면 나머지도 0이어야 함.
        for i in range(len(bits)): 
            if bits[i] == '1':
                return False
        return True
    
    else:
        return chk(bits[:mid], start, mid-1) and chk(bits[mid+1:], mid+1, end)
    

def solution(numbers):
    answer = []
    for n in numbers:
        only_bits = bin(n)[2:]
        length = [1, 3, 7, 15, 31, 63]
        flag = False
        for i in range(len(length)):
            if len(only_bits) == length[i]:
                break
            if len(only_bits) < length[i]:
                while True:
                    only_bits = '0' + only_bits
                    if len(only_bits) == length[i]:
                        flag = True
                        break
            if flag:
                break
        flag = chk(only_bits, 0, len(only_bits))
        if flag:
            answer.append(1)
        else:
            answer.append(0)
        
    return answer
