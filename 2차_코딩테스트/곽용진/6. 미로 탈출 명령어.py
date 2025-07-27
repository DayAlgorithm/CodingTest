from collections import deque

def solution(n, m, x, y, r, c, k):
    x, y, r, c = x-1, y-1, r-1, c-1
    moves = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
    queue = deque()
    queue.append((x, y, 0, ''))
    visited = set()
    visited.add((x, y, 0))
    
    while queue:
        cx, cy, cost, route = queue.popleft()
        if cost > k:
            continue
        
        if cost == k and cx == r and cy == c:
            return route
        
        for dx, dy, drct in moves:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m:
                state = (nx, ny, cost + 1)
                if state not in visited:
                    visited.add(state)
                    queue.append((nx, ny, cost + 1, route + drct))
                    
    return "impossible"
