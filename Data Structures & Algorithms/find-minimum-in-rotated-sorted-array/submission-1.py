class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Bruteforce 
        # mini = nums[0]
        # for i in range(len(nums)):
        #     mini = min(mini, nums[i])
        # return mini

        # Optimized 
        # O(logN) + Sorted = Binary Search

        left = 0
        right = len(nums) - 1

        # Edge Case 
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
        return nums[left]

        """
        [3,4,5,0,1,2]
        mid = 0
        left = 3 | Mid = 0 mid < left: mid = left 
        """


        