class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  
        count = 0  

        start = 0
        while count < n:
            current = start
            prev_value = nums[start]
            while True:
                next_index = (current + k) % n
                nums[next_index], prev_value = prev_value, nums[next_index]
                current = next_index
                count += 1
                if start == current:  
                    break
            start += 1