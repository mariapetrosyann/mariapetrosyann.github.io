class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j]:
                    if abs(i - j) <= k:
                        return True
                    else:
                        return False
