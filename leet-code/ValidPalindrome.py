class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        new_word = word.replace(" ","").replace(",", "").replace(":","").replace(".", "")
        if new_word == "":
            return True
        elif new_word == new_word[::-1]:
            return True     
        else:
            return False
