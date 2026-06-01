class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # bruteforce 

        # for i in range(len(nums) + 1):
        #     if i not in nums:
        #         return i 

        # optimized solution

        """ 
        using XOR op
    
        """
        result = 0
        for i in range(len(nums) + 1):
            result = result ^ i 
        
        for num in nums:
            result = result ^ num
        
        return result

            # Bruteforce

        # for i in range(len(nums) + 1):
        #     if i not in nums:
        #         return i

        # optimized Bitwise Operator

        # result = 0
        # for i in range(len(nums) + 1):
        #     result ^= i

        # """ 
        # 0 ^ 0 = 0 
        # 0 ^ 1 = 1
        # 1 ^ 2 = 3 
        # """

        # for num in nums:
        #     result ^= num

        # """ 
        # 3 ^ 0 = 1 1 ^ 0 0 = 1 1  = 3 
        # 3 ^ 2 = 1 1 ^ 1 0 = 0 1 = 1 
        # """

        # return result
