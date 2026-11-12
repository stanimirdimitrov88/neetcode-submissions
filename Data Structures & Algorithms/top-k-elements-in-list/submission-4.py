class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        a = defaultdict(int)
        
        for idx, val in enumerate(nums): 
            a[val] += 1
        
        # till now we have a = {1: 1, 2: 3, 3: 2}

        buckets = [[] for i in range(len(nums)+1)]
        
        for num in a: 
            buckets[a[num]].append(num)
        # for now [[1], [3], [2]]
        out = []

        for i in range(len(buckets)-1, 0, -1): 
            for j in buckets[i]:
                out.append(j)
                if len(out) == k: 
                    return out
 