class Solution:
    def countComponents(self, n: 'int', edges: 'List[List[int]]') -> 'int':
        if not len(edges):
            return n 
        nodes = {}
        for nd in range(n):
            nodes[nd] = 0
        adj_table = {}
        visited = {}
        stack = []
        
        num_of_comp = 0
        
        for e in edges:
            if e[0] in adj_table:
                adj_table[e[0]].append(e[1])
            else:
                adj_table[e[0]] = [e[1]]
            if e[1] in adj_table:
                adj_table[e[1]].append(e[0])
            else:
                adj_table[e[1]] = [e[0]]
        
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
                