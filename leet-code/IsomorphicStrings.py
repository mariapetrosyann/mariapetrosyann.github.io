class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s=[ch for ch in s]
        t=[ch for ch in t]
        unique_s=len(set(s))
        unique_t=len(set(t))
        if unique_s == unique_t:
            for i in range(len(s)):
                t[i]=s[i]
            if t[i]==s[i]:
                return True
        return False
