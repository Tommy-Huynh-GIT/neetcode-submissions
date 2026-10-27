class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_dict = {}
        
        for s in strs:
            sorted_string = ''.join(sorted(s))
            if sorted_string in sorted_dict:
                #append value to array
                sorted_dict[sorted_string].append(s)
            #create new key value pair
            else:
                sorted_dict[sorted_string] = [s]

        returned_array = list(sorted_dict.values())
        return returned_array