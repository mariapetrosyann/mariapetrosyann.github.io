class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:]+ nums[:-k]

        # i = 0
        # while i <  k:
        #     nums[:] = [nums[-1]]+ nums[:-1]
        #     i += 1        
