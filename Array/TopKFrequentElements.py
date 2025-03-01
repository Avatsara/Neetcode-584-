class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}  
        res = []
        for num in nums: 
            if num not in hmap: 
                hmap[num] =1 
            else: 
                hmap[num]+=1 
        sorted_dict= dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True))
        res = list(sorted_dict.keys())[:k] 

        return res