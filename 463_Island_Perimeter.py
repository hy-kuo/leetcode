class Solution:
    def islandPerimeter(self, grid: 'List[List[int]]') -> 'int':
        if len(grid) == 0:
            return 0
        i = len(grid)
        j = len(grid[0])
        def is_grid(index):
            
            if index[0] < 0 or index[0] >= i:
                return False
            if index[1] < 0 or index[1] >= j:
                return False
            return True
        def neighbors(index):
            directs = [(0,1), (1,0),(-1,0),(0,-1)]
            ns = 0
            for d in directs:
                if is_grid((index[0]+d[0], index[1]+d[1])) and grid[index[0]+d[0]][index[1]+d[1]] == 1:
                    ns += 1
            return ns
        ans = 0
        for i_idx in range(i):
            for j_idx in range(j):
                if grid[i_idx][j_idx] == 1:
                    ans += 4-neighbors((i_idx, j_idx))
        return ans 