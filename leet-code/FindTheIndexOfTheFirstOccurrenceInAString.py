class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)- len(needle)+1):
            midle_needle = i+len(needle)
            if haystack[i:midle_needle] == needle:
                return i
        return -1
