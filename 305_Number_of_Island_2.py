class Solution:
    def numIslands2(self, m: 'int', n: 'int', positions: 'List[List[int]]') -> 'List[int]':
        self.table = {}
        self.island = {}
        ans = []
        num_of_island = 0
        for p in positions:
            nbrs = self.neighbors(p, m, n)
            new_island_f = True
            nbr_island = set()
            for nbr in nbrs:
                if nbr in self.table:
                    nbr_island.add(self.table[nbr])
                    new_island_f = False                    
                    
            if new_island_f:
                self.table[(p[0], p[1])] = num_of_island
                self.island[num_of_island] = [p]
                num_of_island +=1
            else:
                self.update_island(p, nbr_island)
               
            ans.append(len(set(self.island.keys())))
        return ans
    
    
    def update_island(self, p, nbr_island):
        nbr_island = list(nbr_island)
        min_i = min(nbr_island)

        lands = [p]
        for i in nbr_island:
            lands += self.island[i]
        for i in nbr_island:
            del self.island[i]
        for l in lands:
            self.table[(l[0], l[1])] = min_i
        self.island[min_i] = lands
        
        
        
        
    def neighbors(self, idx: 'List[int]', m, n):
        
        direct = [[1,0], [0,1], [-1,0], [0,-1]]
        neighbors = [(idx[0]+d[0], idx[1]+d[1]) for d in direct]
        neighbors = [nbr for nbr in neighbors if nbr[0]>=0 and nbr[1]>=0 and nbr[0]<m and nbr[1]<n]
        
        return neighbors
        