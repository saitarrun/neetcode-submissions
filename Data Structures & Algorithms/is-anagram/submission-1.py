from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # Solution One : Use sorted() function

        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False
        

        # Solution 2: use Counter() from Collections to count 
        return Counter(s) == Counter(t)