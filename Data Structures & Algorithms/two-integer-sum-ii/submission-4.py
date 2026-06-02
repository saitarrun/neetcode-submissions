class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers)-1
            while left <= right:
                mid = (left + right)//2
                current_sum = numbers[i] + numbers[mid]
                if current_sum == target:
                    return [i + 1, mid + 1]
                # [ 1 2 3 4 ]
                elif current_sum < target:
                    left = mid + 1 
                else:
                    right = mid - 1
        return []                

                
            
                
        
        