class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #put str into key value pairs and compare the key value pairs of both
            
        sDict = {}
        for letter in s:
            #if letter already exists
            if letter in sDict:
                #get old val
                oldVal = sDict.get(letter)
                #create new val based off old val
                newVal = oldVal + 1
                #update val
                sDict.update({letter : newVal})
            else:
                #if letter doesn't exist
                sDict[letter] = 0
          
        tDict = {}
        for letter in t:
            #if letter already exists
            if letter in tDict:
                #get old val
                oldVal = tDict.get(letter)
                #create new val based off old val
                newVal = oldVal + 1
                #update val
                tDict.update({letter : newVal})
            else:
                #if letter doesn't exist
                tDict[letter] = 0
            
        tDictKeys = tDict.keys()
        sDictKeys = sDict.keys()
        if len(sDictKeys) != len(tDictKeys):
            return False

        #Loop through a set of whichever keys you want
        #Have to think about if sentence length is the same or not

        for key in tDictKeys:
            #if the key isn't in the other dictionary no way it's anagram
            if key not in sDictKeys:
                return False
            else:
                #check every key and compare values
                val1 = tDict[key]
                val2 = sDict[key]
                if(val1 != val2):
                    return False
        return True


