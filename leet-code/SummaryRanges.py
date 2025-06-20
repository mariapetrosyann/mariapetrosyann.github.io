class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        results = []
        first_element = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if first_element == nums[i-1]:
                    results.append(str(first_element))
                else:
                    results.append(f"{first_element}->{nums[i-1]}")
                first_element = nums[i]
        if first_element == nums[-1]:
            results.append(str(first_element))
        else:
            results.append(f"{first_element}->{nums[-1]}")
    
        return results
