from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # bruteforce 

        # input : string s t 
        # find : anagrams : same freq
        # output: if anagram : true else false

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # if sorted_s == sorted_t:
        #     return True
        # return False

        # time complexity : o(n) + O(m) = O(n + m)

        # Counter 

        count_S = Counter(s)
        count_t = Counter(t)

        if count_S == count_t:
            return True
        return False




        
