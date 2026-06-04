class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[left] <= nums[mid]:
            # 3 <= 6 
                if target > nums[mid] or target < nums[left]:
                    # 1 > 6 or 1 < 3 
                    left = mid + 1
                else:
                    right = mid - 1 
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1 
        return -1

