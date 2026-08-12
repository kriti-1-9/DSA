class Solution(object):
    def trapRainWater(self, heightMap):
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []  # (height, row, col)

    # Step 1: Push all boundary cells into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        trapped_water = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

    # Step 2: Process heap
        while heap:
            height, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    neighbor_height = heightMap[nr][nc]

                # If neighbor is lower, water can be trapped
                    if neighbor_height < height:
                        trapped_water += height - neighbor_height

                # Push max boundary height
                    heapq.heappush(heap, (max(height, neighbor_height), nr, nc))

        return trapped_water