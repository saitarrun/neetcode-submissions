class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # bruteforce 

        # basecase if the len(s) != len(t) : False

        if len(s) != len(t) : return False

        # if the count of s == t: True 

        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True
        
