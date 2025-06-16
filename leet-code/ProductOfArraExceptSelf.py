class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        for num in nums:
            if num != 0:
                total_product *= num

        result = []
        for num in nums:
            if num == 0:
                result.append(total_product)
            else:
                result.append(0 if 0 in nums else total_product // num)
        return result
       
