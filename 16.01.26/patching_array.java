class Solution {
    //greedily add that number which can for largest sequence of numbers till n or more
    public int minPatches(int[] nums, int n) {
        long miss = 1;
        int i = 0;
        int result = 0;

        while(miss <= n){
            //value is present
            if(i < nums.length && nums[i] <= miss){
                miss += nums[i];
                i++;
            }
            else{
                //value is absent and insert previous miss and 
                //btata hai kisi bhi no. ko add krke 4 bna nahi
                miss += miss;      //btata hai ab value miss tk bn jaigi
                result++;
            }
        }
        return result;
    }
}
