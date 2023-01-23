class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_chars = {}
        slow = fast = 0
        max_length = 0
        for char in s:
            while(char in substring_chars.values()):
                del substring_chars[slow]
                slow += 1
            substring_chars[fast] = char
            fast += 1
            max_length = max(max_length, fast - slow)
        return max_length
