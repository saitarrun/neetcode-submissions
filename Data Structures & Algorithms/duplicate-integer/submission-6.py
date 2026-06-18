class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # input : array[nums]
        # to find : duplicates : True 

        # bruteforce

        # num = len(nums)
        # for i in range(num):
        #     for j in range(i+1, num):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # optimized 

        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False