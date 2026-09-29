class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1

        if not s:
            return s

        while l <= r:

            temp1 = s[l]
            temp2 = s[r]

            s[l] = temp2
            s[r] = temp1

            l += 1
            r -= 1
        
        return s

        