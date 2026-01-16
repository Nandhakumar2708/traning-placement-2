class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [[-1] * n for _ in range(m)]

        def f(row , col):
            if row == col == 0:
                return 1

            if dp[row][col] != -1:
                return dp[row][col]
            
            left , up = 0 , 0
            
            if row - 1 >= 0 and obstacleGrid[row - 1][col] != 1:
                left = f(row - 1 , col)

            if col - 1 >= 0 and obstacleGrid[row][col - 1] != 1:
                up = f(row , col - 1)


            dp[row][col] = left + up
            return dp[row][col]

        return f(m - 1 , n - 1)



             




        
        

        
