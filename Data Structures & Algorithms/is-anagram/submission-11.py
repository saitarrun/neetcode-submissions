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

        # count_S = Counter(s)
        # count_t = Counter(t)

        # if count_S == count_t:
        #     return True
        # return False

        # hashmap 
        freq_s = {}
        freq_t = {}

        for char in s:
            freq_s[char] = freq_s.get(char,0) + 1
        
        # increasing the frequency_s 

        for char in t:
            freq_t[char] = freq_t.get(char,0) + 1

        return freq_s == freq_t
        








        
