class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        prefix = []
        current_max = nums[0]

        for x in nums:
            current_max = max(current_max, x)
            prefix.append(self.gcd(x, current_max))

        prefix.sort()

        left, right = 0, len(prefix) - 1
        ans = 0

        while left < right:
            ans += self.gcd(prefix[left], prefix[right])
            left += 1
            right -= 1

        return ans