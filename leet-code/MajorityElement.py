class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        for num in nums:
            if num in majority:
                majority[num] +=1
            else:
                majority[num] = 1
        max_count = 0
        most_repeted = None
        for num in majority:
            if majority[num] > max_count:
                max_count = majority[num]
                most_repeted = num
        return most_repeted
        
