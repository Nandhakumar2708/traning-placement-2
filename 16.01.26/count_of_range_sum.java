class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        long[] prefixSum = new long[nums.length];
        int count = 0;
        List<Long> ls = new ArrayList<>();
        prefixSum[0]=nums[0];
        for (int i = 1; i < nums.length; i++) prefixSum[i]=nums[i]+prefixSum[i-1];
        if (lower <= nums[0] && nums[0] <= upper) count++;
        ls.add(prefixSum[0]);
        //ps[i]-x >= lower -> x <= ps[i]-lower
        //ps[i]-x <= upper -> x >= ps[i]-upper
        // want all x less than or equal to ps[i]-lower
        // want all x greater than or equal to ps[i]-upper
        // get first occurrence of ps[i]-lower+1 and subtract 1 to get last occ of ps[i]-lower
        // get first occ of ps[i]-upper
        for (int i = 1; i < nums.length; i++) {
            if (lower <= prefixSum[i] && prefixSum[i] <= upper) count++;
            long hi = prefixSum[i]-lower+1;
            long lo = prefixSum[i]-upper;
            int lowIdx = customBinarySearch(ls, lo);
            int hiIdx = customBinarySearch(ls, hi);
            count += (hiIdx-lowIdx);
            int idx = Collections.binarySearch(ls, prefixSum[i]);
            if (idx < 0) idx = -(idx+1);
            ls.add(idx, prefixSum[i]);
        }
        return count;
    }
    // find smallest instance of x -1;
    private int customBinarySearch(List<Long> list, Long target) {
        int left = 0;
        int right = list.size() - 1;
        int result = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (list.get(mid) < target) {
                result = mid;      // mid is a valid candidate
                left = mid + 1;    // try to find a larger index
            } else {
                right = mid - 1;
            }
        }

        return result;

    }
}
