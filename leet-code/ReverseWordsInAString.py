class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        w = s.split(" ")
        words = [word for word in w if word !='']
        results = " ".join(words[::-1])
        return results
