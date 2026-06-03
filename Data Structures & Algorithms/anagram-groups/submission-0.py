class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Keys = letters, values = []
        #used the sorted function

        #create dictionary to hold key value pairs
        anagram_dict = {}

        #loop over the list of strings
        for string in strs:
            #sort the current string in alphabetical order to be used as a key
            sorted_string = sorted(string) #returns list of letters
            ordered_string = "".join(sorted_string)
            #if the key doesn't exist
            if ordered_string not in anagram_dict.keys():
                #add the key + value 
                anagram_dict.update({ordered_string : [string]})
            else: 
                #append a new value
                anagram_dict[ordered_string].append(string)

        returned_list = []

        for value in anagram_dict.values():
            returned_list.append(value)

        return returned_list