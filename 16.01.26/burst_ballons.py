class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length;
        int[] balloons = new int[n+2];
        balloons[0]=1;
        balloons[n+1]=1;

        for(int i=0;i<n;i++){
            balloons[i+1] = nums[i];
        }
        int[][] dp = new int[n+2][n+2];

        for(int i=1;i<=n;i++){
            for(int j=0;j<n-i+1;j++){
                int right = j+i+1;
                if(right > n+1) continue;

                for(int k = j+1;k<right;k++){
                    int coin = dp[j][k]+dp[k][right]+balloons[j]*balloons[k]*balloons[right];
                    dp[j][right]= Math.max(dp[j][right], coin);
                }
            }
        }
         return dp[0][n+1];
    }
}
