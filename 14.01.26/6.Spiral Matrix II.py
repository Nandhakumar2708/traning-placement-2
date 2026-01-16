class Solution(object):
    def generateMatrix(self, n):
        matrix=[[1 for _ in range(n)]for _ in range(n)]
        i,j=0,0
        k=0
        for nb in range(2,n*n+1):
            if j==k and i<n-1:
                i+=1
                matrix[j][i]=nb
            elif i==n-1 and j<n-1:
                j+=1
                matrix[j][i]=nb
            elif j==n-1 and i>k:
                i-=1
                matrix[j][i]=nb
            else:
                j-=1
                matrix[j][i]=nb
            if i==k and j==n-1:
                k+=1
                n-=1
        return matrix
