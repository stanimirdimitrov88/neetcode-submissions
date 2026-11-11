class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        a = defaultdict(int)
        
        for idx, val in enumerate(nums): 
            a[val] += 1

        # till now we have a = {1: 6, 2: 3, 3: 2}

        #a = {1: 1, 2: 3, 3: 10}
        #print(max(a.items()))
      
        top_k = []

        for i in range(k):
            max_ = max_item = max(a.items(), key=lambda item: item[1])
            top_k.append(max_[0])
            a.pop(max_[0])

        return top_k
             