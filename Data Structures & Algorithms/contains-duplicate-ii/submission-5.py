class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        if not nums and k == 0:
                return False

        for i, num in enumerate(nums):
            
            if num not in seen:
                seen[num] = i

            elif num in seen:
                if abs(i - seen[num]) <= k:
                    return True
            seen[num] = i

        return False