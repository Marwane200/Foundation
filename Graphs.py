
# == BREADTH FIRST SEARCH ==
# Leet Code 1293: Shortest Path in a Grid - https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Return the minimum number of steps to walk from the upper left corner to the lower right corner,
# you can eliminate at most `k` obstacles. If none return -1.
from collections import deque
def shortestPath(grid: list[list[int]], k: int) -> int:

    ROWS = len(grid)
    COLS = len(grid[0])

    que = deque([])
    start = (0,0,k,0)
    end = (ROWS-1,COLS-1)

    visited = set()
    que.append(start)
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    while que:
        x,y,k1,count = que.popleft()
        if (x,y) == end: return count

        for v in range(4):
            x2,y2 = x + dx[v], y + dy[v]
            if 0 <= x2 < ROWS and 0 <= y2 < COLS:
                k2 = k1 - grid[x2][y2]
                if (x2,y2,k2) in visited: continue
                if k2 < 0: continue
                visited.add((x2,y2,k2))
                que.append((x2,y2,k2,count+1))
    
    return -1


# == DEPTH FIRST SEARCH ==
# Leet Code 79: Word Search - https://leetcode.com/problems/word-search/
# Given an m x n grid of characters board and a string word,
# return true if word exists in the grid.
def wordSearch(board: list[list[str]], word: str) -> bool:

    ROWS = len(board)
    COLS = len(board[0])

    visited = set()
    dx = [0,1,0,-1]
    dy = [-1,0,1,0] 

    def dfs(x,y,i):
        if i == len(word): return True
        if (x,y) in visited: return False
        if 0 <= x < ROWS and  0 <= y < COLS:
            if board[x][y] != word[i]: return False
            visited.add((x,y))

            for v in range(4):
                x2,y2 = x + dx[v], y + dy[v]
                if dfs(x2,y2,i+1): return True
            visited.remove((x,y))

        return False


    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == word[0]:
                if dfs(i,j,0): return True
    return False