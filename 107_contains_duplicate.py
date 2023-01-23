class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tracker = set()
        for num in nums:
            if num in tracker:
                return True
            else:
                tracker.add(num)
        return False
