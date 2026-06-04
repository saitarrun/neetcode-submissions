class Solution:
    def isPalindrome(self, s: str) -> bool:
        strRes = ""
        for c in s:
            if c.isalnum():
                strRes += c.lower()
        return strRes == strRes[::-1]
        