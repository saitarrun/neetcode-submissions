class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # input : list 
        # output: indexes

        # bruteforce - O(n^2)

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # hashmap

        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]] = i
        return []










        