class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use hashmap to hold occurences of each number then return the top k 

        num_dict = {}

        for num in nums:
            if num not in num_dict:
                num_dict.update({num : 1})
            else:
                num_dict[num] += 1

        #sort from ascending to descending
        num_dict = dict(sorted(num_dict.items(), key=lambda x: x[1], reverse=True))
    
        keys = list(num_dict.keys())[:k]
        return keys

