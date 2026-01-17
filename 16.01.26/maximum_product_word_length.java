class Solution {
    public int maxProduct(String[] words) {
        

        int[] dp=new int[words.length];

        for(int i=0;i<words.length;i++){
            for(int j=0;j<words[i].length();j++){
                dp[i] |= 1 << (words[i].charAt(j) - 'a');
            }
        }

        int maxProductLen=0;

        for(int i=0;i<words.length;i++){
            for(int j=i+1;j<words.length;j++){
                if((dp[i] & dp[j]) == 0){
                    maxProductLen=Math.max(maxProductLen,words[i].length() * words[j].length());
                }
            }
        }

        return maxProductLen;
    }
}
