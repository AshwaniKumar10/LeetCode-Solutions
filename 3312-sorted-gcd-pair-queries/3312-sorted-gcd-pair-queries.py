class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        mx = max(nums)
        
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        
        divCnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for m in range(g, mx + 1, g):
                divCnt[g] += freq[m]

        
        exact = [0] * (mx + 1)

        for g in range(mx, 0, -1):
            pairs = divCnt[g] * (divCnt[g] - 1) // 2
            m = g * 2
            while m <= mx:
                pairs -= exact[m]
                m += g
            exact[g] = pairs

        
        prefix = [0] * (mx + 1)
        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        
        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))

        return ans