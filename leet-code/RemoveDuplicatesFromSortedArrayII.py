class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fix_index = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[fix_index - 2]:
                nums[fix_index] = nums[i]
                fix_index += 1
        
        return fix_index
         
