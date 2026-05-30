class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #O(n^2)
        #for i in range(len(nums)): 
           # for j in range(i + 1, len(nums)):
               # if((nums[i] + nums[j]) == target):
                    #return [i,j]

        #Hashmap solution
        num_keys = {} # value : index
        #insert keys in hashmap for quick lookup 
        for i, num in enumerate(nums):
            num_want = target - num
            if num_want in num_keys:
                return [num_keys[num_want], i]
            num_keys[num] = i

                