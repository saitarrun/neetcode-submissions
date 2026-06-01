class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # bruteforce; 
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        
        # Hashset

        # hashset = set()
        # for i in range(len(nums)):
        #     complement = target - nums[i]   # 7 - 3 = 4 
        #     if complement in hashset:
        #         complement_index = nums.index(complement)   # Find the index of the complement nums.index(complement)
        #         return [complement_index, i]
        #     hashset.add(nums[i])
        # return []


        # Dict
        hashdict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashdict:
                return [hashdict[complement],i]
            hashdict[nums[i]] = i 
        return []


