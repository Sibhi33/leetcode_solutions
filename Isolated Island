class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        island_map = [[(grid[r][c], 0) for c in range(n)] for r in range(n)]
        visited = [[False] * n for _ in range(n)]
        
        def bfs(r, c, num):
            q = deque([(r, c)])
            cells = []
            while q:
                r, c = q.popleft()
                if visited[r][c]: continue
                visited[r][c] = True
                cells.append((r, c))
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc]:
                        q.append((nr, nc))
            size = len(cells)
            for r, c in cells:
                island_map[r][c] = (size, num)
            return size

        island_sizes, num, max_island = {}, 1, 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] and not visited[r][c]:
                    island_sizes[num] = bfs(r, c, num)
                    max_island = max(max_island, island_sizes[num])
                    num += 1
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    neighbors = set()
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and island_map[nr][nc][0]:
                            neighbors.add(island_map[nr][nc][1])
                    
                    new_size = 1 + sum(island_sizes[i] for i in neighbors)
                    max_island = max(max_island, new_size)

        return max_island
