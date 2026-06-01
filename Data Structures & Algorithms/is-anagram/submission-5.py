from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # base condition 
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)