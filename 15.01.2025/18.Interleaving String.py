class Solution:
    def solve(self, x, y, z, s1, s2, s3, dp):
        if x == 0 and y == 0 and z == 0:
            return True
        if dp[x][y] != -1:
            return dp[x][y]
        a, b = False, False
        if x - 1 >= 0 and z - 1 >= 0 and s1[x - 1] == s3[z - 1]:
            a = self.solve(x - 1, y, z - 1, s1, s2, s3, dp)
        if y - 1 >= 0 and z - 1 >= 0 and s2[y - 1] == s3[z - 1]:
            b = self.solve(x, y - 1, z - 1, s1, s2, s3, dp)
        dp[x][y] = a or b
        return dp[x][y]

    def isInterleave(self, s1, s2, s3):
        x, y, z = len(s1), len(s2), len(s3)
        dp = [[-1] * (y + 1) for _ in range(x + 1)]
        return self.solve(x, y, z, s1, s2, s3, dp)
