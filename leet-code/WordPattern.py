class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_pattern_to_s = {}
        pattern=[ch for ch in pattern]
        s=s.split()
        if len(pattern) != len(s):
            return False
        for chars, words in zip(pattern, s):
            if chars in map_pattern_to_s:
                if map_pattern_to_s[chars] != words:
                    return False
            map_pattern_to_s[chars] = words
        return True
