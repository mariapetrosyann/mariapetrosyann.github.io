class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_lenght = 0
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_lenght = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_lenght += 1
                longest_lenght = max(longest_lenght, current_lenght)
        return longest_lenght
