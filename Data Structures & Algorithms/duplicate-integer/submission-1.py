class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = {}
        for i, k in enumerate(nums): 
            if k in seen: 
                return True
            else:
                seen[k] = i
        return False
            