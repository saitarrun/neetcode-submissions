from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # Solution One : Use sorted() function

        # return sorted(s) == sorted(t)
        

        # Solution 2: use Counter() from Collections to count 
        # return Counter(s) == Counter(t)

        # Solution 3: Hashmap Implementation

        if len(s) != len(t):  # check if they are palindrome
            return False
        
        countS, countT = {}, {}  # initalise Hashmaps

        for i in range(len(s)):     
            countS[s[i]] = 1 + countS.get(s[i],0) 
            countT[t[i]] = 1 + countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
        
