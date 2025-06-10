class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        word = words[-1]
        count = len(word)
        return count
        
