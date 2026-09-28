class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDupe = []
        for num in nums:
            if num in noDupe:
                return True
            noDupe.append(num)
        
        return False