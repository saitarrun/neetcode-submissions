class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # base cases: do we have any dup elems 
        # what if the array/list = []
        # Single element return the [ele] / False 
        # Constraints is <= 1000
        # O(n^2) or O(nlogn)

        # bruteforce 

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]
        # return []


        # Optimised using a set or hashmap

        hashset = set()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashset:
                complement_index = nums.index(target-nums[i])
                return [complement_index, i]
            hashset.add(nums[i])
        return []
        
        
        # num_map = {}
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in num_map:
        #         return [num_map[complement],i]
        #     num_map[nums[i]] = i
        # return []