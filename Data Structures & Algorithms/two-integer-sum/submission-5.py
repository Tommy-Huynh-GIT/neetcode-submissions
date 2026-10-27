class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use enum to get both index and value 
        seen = {}

        for i,nums in enumerate(nums):
            # 7 - 3 = 4
            complement = target - nums

            # 4
            if complement in seen:
                return[seen[complement], i]
        
            seen[nums] = i

            