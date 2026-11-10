class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        a = {}
        for index, value in enumerate(nums): 
            a[value] = index

        output = []
        for index, value in enumerate(nums):
            diff = target - value
            if (diff in a) and a[diff] != index:
                return [index, a[diff]]
            
        return output
        