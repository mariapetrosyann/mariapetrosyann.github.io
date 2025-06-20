class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        idx = 0
        for i in range(len(citations)):
            if citations[i] >= i+1:
                idx = i+1
            else:
                break
        return idx
