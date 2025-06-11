class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = 0
        i = 0
        for i in range(len(magazine)):
            for j in range(len(ransomNote)):
                if ransomNote[j] == magazine[i]:
                    count += 1
                    break
        if count == len(ransomNote):
            return True
        return False
