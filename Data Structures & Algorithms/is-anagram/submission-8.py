from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # bruteforce 

        # basecase if the len(s) != len(t) : False

        # if len(s) != len(t) : return False

        # # if the count of s == t: True 

        # for char in set(s):
        #     if s.count(char) != t.count(char):
        #         return False
        # return True

        # counters

        # return Counter(s) == Counter(t)

        # sorted 

        # return sorted(s) == sorted(t)


        

        if len(s) != len(t):

            return False

        freq_s = {}

        freq_t = {}

        for ch in s:

            freq_s[ch] = freq_s.get(ch,0) + 1

        for ch in t:

            freq_t[ch] = freq_t.get(ch,0) + 1

    
        return freq_s == freq_t 
        
