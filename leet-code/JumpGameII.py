class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        count = 0
        last_index = len(nums) - 1
        while i < last_index:
            max_jump = nums[i]
            if max_jump == 0:
                count = 0
                return count
            
            best_index = i + 1
            max_val = nums[best_index]
            for j in range(i + 1, min(i + max_jump + 1, len(nums))):
                if nums[j] > max_val:
                    best_index = j
                    max_val = nums[j]
    
            i = best_index
            count += 1
            if i >= last_index:
                return count
        return count
