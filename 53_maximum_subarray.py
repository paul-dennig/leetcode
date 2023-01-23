class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = 0
        total_max = -inf
        for num in nums:
            current_max = max(num, num+current_max)
            total_max = max(current_max, total_max)
        return total_max
