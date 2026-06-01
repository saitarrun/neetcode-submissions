class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # Solution One : Use sorted() function

        if sorted(s) == sorted(t):
            return True
        else:
            return False
        