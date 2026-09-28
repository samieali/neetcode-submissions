class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s = sorted((item.replace(" ", "").lower() for item in s))
        new_t = sorted((item.replace(" ", "").lower() for item in t))
        if new_s == new_t:
            return True
        else: return False
