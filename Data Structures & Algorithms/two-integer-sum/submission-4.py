class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Bruteforce method
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []



        # hashMap: 
        hashmap = {}
        for i,num in enumerate(nums): # needs to find the index
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i        #enter the num in the hashmap at index i
        return 