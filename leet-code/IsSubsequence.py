class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        i = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if t[j] == s[i]:
                    count += 1
                    break
        if count == len(s):
            return True
        return False  
