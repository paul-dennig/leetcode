class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for char in s:
            if (char not in letters):
                letters[char] = 1
            else:
                letters[char] = letters[char] + 1
        sum = 0
        hasOdd = False
        for char in letters:
            if (letters[char] % 2 == 1):
                hasOdd = True
            sum = sum + letters[char] - (letters[char] % 2)
        if (hasOdd):
            return sum + 1
        else:
            return sum
