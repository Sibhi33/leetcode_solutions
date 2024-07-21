class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(conditions):
            graph = defaultdict(list)
            indegree = {i: 0 for i in range(1, k + 1)}
            
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            
            zero_indegree = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            order = []
            
            while zero_indegree:
                node = zero_indegree.popleft()
                order.append(node)
                
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        zero_indegree.append(neighbor)
            
            if len(order) != k:
                return []
            
            return order
        
        row_order = topological_sort(rowConditions)
        if not row_order:
            return []
        
        col_order = topological_sort(colConditions)
        if not col_order:
            return []
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix
