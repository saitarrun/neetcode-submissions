class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """"
        m*n matrix and target 
        each row: ascending 
        return true if found else false
        """

        """"
        Time Complexity: bruteforce = O(m * n)
        Optimimzed : O(log(m*n))
        """ 

        # bruteforce 
        # change into columns and rows 
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
                
        return False
        