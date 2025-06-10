class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            i=0
            while i < len(prefix) and i < len(s):
                if prefix[i] == s[i]:
                  i += 1
                else:
                  break
            prefix = prefix[:i]
        if prefix == "":
            return ""
        return prefix
