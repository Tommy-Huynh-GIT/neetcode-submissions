class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #First lets check if lengths are the same otherwise its not an anagram
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        #Put each char as a key in a hashmap and value as the number of occurences, if the key exist add to the value if not create a new key value pair
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1

        #now we check a key, if it exists in the other dict if it does look at the value if that matches go to the next key
        return s_dict == t_dict
        
        #Dictionaries are fundamentally key → value mappings. Equality is based on the contents, not the order.