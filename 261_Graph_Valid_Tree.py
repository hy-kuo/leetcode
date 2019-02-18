class Solution:
    def validTree(self, n: 'int', edges: 'List[List[int]]') -> 'bool':
        
        adj_table = {}
        visited = {}
        visited_edge = {}
        stack = []
        if not len(edges):
            if n==1:
                return True
            else:
                return False
        for e in edges:
            if e[0] not in adj_table:
                adj_table[e[0]] = [e[1]]
            else:
                adj_table[e[0]].append(e[1])
            if e[1] not in adj_table:
                adj_table[e[1]] = [e[0]]
            else:
                adj_table[e[1]].append(e[0])

        is_tree = True
        node = edges[0][0]
        stack.append(node)
        while(len(stack)):
            node = stack.pop()
            if node in visited:
                continue
            visited[node] = True
            adjs = adj_table[node]
            for adj in adjs:
                a, b = min(node, adj), max(node,adj)
                if adj in stack and (a,b) not in visited_edge:
                    is_tree = False
                    break
                elif adj not in visited:
                    stack.append(adj)
                visited_edge[(a,b)] = True
                
            if not is_tree:
                break
        
        if len(visited) != n:
            is_tree = False
        return is_tree
            
            
        