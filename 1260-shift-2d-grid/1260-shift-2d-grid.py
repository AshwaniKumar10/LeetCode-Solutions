class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])

        arr = []

        
        for row in grid:
            arr.extend(row)

        total = m * n
        k %= total

        
        arr = arr[-k:] + arr[:-k]

        
        ans = []
        idx = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[idx])
                idx += 1
            ans.append(row)

        return ans