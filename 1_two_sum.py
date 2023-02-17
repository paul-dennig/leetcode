
"""
prompt: #1 https://leetcode.com/problems/two-sum/
"""

class Solution:
    
    def twoSum(self, nums, target):
        return self.solution1(nums, target)
    
    def solution1(self, nums, target):
        compliments = {}
        for i, num in enumerate(nums):
            compliment = target-num
            if num in compliments:
                return [compliments[num], i]
            else:
                compliments[compliment] = i
        return compliments

    @staticmethod
    def test(self):
        
        # test example 1
        numsExample1 = [2, 7, -1, 11]
        targetExample1 = 9
        resultExample1 = [1, 2]

        # test example 2
        numsExample2 = [3, 3]
        targetExample2 = 6
        resultExample2 = [0, 1]

        # invoke test
        assert resultExample1 == self.twoSum(numsExample1, targetExample1)
        assert resultExample2 == self.twoSum(numsExample2, targetExample2)

# Comment the next line out if copy pasting into the Leetcode editor
Solution.test()