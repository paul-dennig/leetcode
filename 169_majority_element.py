class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        guess = ""
        counter = 0
        for num in nums:
            if (counter == 0):
                guess = num
                counter = 1
            elif (num == guess):
                counter = counter + 1
            else:
                counter = counter - 1
        return guess
            
