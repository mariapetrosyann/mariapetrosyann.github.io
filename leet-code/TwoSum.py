class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results=[]
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                two_sum= nums[i]+nums[j]
                if two_sum==target:
                    results.append(i)
                    results.append(j)
            if results!=[]:
                break
        return results
