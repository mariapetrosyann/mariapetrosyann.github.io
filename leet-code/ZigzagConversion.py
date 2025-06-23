class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ''
        for row in range(numRows):
            steps = 2 * (numRows -1)
            for i in range(row, len(s), steps):
                result += s[i]
                if(row > 0 and row < numRows -1 and i + steps - 2 * row < len(s)):
                    result += s[i + steps - 2 * row]
    
        return result
