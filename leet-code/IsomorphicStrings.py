class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        unique_s=len(set([ch for ch in s]))
        unique_t=len(set([ch for ch in t]))
        if unique_s != unique_t:
            return False
        map_s_to_t = {}
        for i, j in zip(s, t):
            if i in map_s_to_t:
                if map_s_to_t[i] != j:
                    return False
            map_s_to_t[i]=j
        return True
