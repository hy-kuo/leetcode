class Solution:
    def findCircleNum(self, M: 'List[List[int]]') -> 'int':

        nodes = {}
        n = len(M)
        for nd in range(n):
            nodes[nd] = 0
        adj_table = {}
        visited = {}
        stack = []
        num_of_comp = 0
        for idx_i, row in enumerate(M):
            for idx_j, p in enumerate(row):
                if idx_i == idx_j:
                    continue
                if p:
                    if idx_i not in adj_table:
                        adj_table[idx_i] = [idx_j]
                    else:
                        adj_table[idx_i].append(idx_j)
                    
        while len(visited) < n:
            nd = list(nodes.keys())[0]
            del nodes[nd]
            visited[nd] = True
            num_of_comp += 1
            if nd in adj_table:
                stack = [adj for adj in adj_table[nd] if adj not in visited]
            else:
                continue
            while len(stack):
                nd = stack.pop()
                stack += [adj for adj in adj_table[nd] if adj not in visited]
                if nd not in visited:
                    del nodes[nd]
                    visited[nd] = True
        return num_of_comp

                