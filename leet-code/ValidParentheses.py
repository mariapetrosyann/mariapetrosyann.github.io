class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[': ']'}
        count = 0
        for i in range(len(s)):
            for j in range(1, len(s)):
                if s[j] == pairs.get(s[i]) and j>i:
                    if (j-(i+1))%2==0 or j-i==1:
                        count += 1
        if count == len(s)//2 and count != 0:
            return True
        return False
