class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        fpt= 0
        spt = n-1

        while fpt <spt:  
            if numbers[fpt]+numbers[spt]>target: 
                spt-=1 
            elif numbers[fpt]+numbers[spt]<target: 
                fpt+=1 
            else: 
                return [fpt+1,spt+1]