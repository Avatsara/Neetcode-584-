class Solution: 
    def majorityElement(self, nums: List[int]) -> int: 
        count = {}
        for num in nums:  
            if num in count: 
                count[num] += 1 
            else: 
                count[num] = 1 
        
        max_value = max(count.values()) 
  
        for key, value in count.items(): 
            if value == max_value: 
                return key
        return -1