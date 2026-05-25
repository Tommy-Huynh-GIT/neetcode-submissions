class Solution:
    #parameters, self, nums which should be a List of ints
    # and returns bool 
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Put the list into a set to get unique values
        #set those unique values as keys for the hash table and set values to 0
        #if value is ever accessed in the hash table and incremented then return true
        #if we go through the whole list without copies return false


        #this solution is bad I could have just checked the length of the set compared to the 
        #to the length of the list and if it's different then there's a solution

        if (len(nums) != len(set(nums))):
            return True
        return False
