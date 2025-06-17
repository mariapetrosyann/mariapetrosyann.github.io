class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        results=[]
        for i in range(len(numbers)):
            for j in range(1,len(numbers)):
                two_sum= numbers[i]+numbers[j]
                if two_sum==target:
                    results.append(i+1)
                    results.append(j+1)
            if results!=[]:
                break
        return results
