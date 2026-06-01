class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for i in nums:
            if i in duplicate:
                return True
            duplicate.add(i)
        return False