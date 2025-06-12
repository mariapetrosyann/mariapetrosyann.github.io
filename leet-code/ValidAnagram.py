class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unique_s=set([ch for ch in s])
        unique_t=set([ch for ch in t])
        if unique_s == unique_t:
            return True
        return False
