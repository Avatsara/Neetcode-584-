class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        
        if 0 in freq and freq[0] > 2:
            result.append([0, 0, 0])

      
        for num in freq:
            if num != 0 and freq[num] > 1:
                complement = -2 * num
                if complement in freq:
                    result.append([num, num, complement])

        unique_nums = sorted(freq.keys())
        for i in range(len(unique_nums)):
            num1 = unique_nums[i]
            if num1 > 0:
                break

            for j in range(i + 1, len(unique_nums)):
                num2 = unique_nums[j]
                complement = -num1 - num2

              
                if complement > num2 and complement in freq:
                    result.append([num1, num2, complement])

        return result