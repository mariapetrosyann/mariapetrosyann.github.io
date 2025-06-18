class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        subarray = []
        for i in range(len(nums)):
            if nums[i] == target:
                subarray.append(nums[i])
                break
            for j in range(i + 1, len(nums)):
                total = nums[i] + nums[j]
                if total == target:
                    subarray.append(nums[i])
                    subarray.append(nums[j])
                    break
            if subarray:
                break

        return len(subarray)
