class Solution {
    public void wiggleSort(int[] nums) {
        int n = nums.length;
        int median = kth(nums, (n+1)/2);

        int left = 0;
        int right = n - 1;
        int i = 0;

        while (i <= right){
            int mi = map(i,n);
            if (nums[mi] > median){
                swap(nums, map(left++, n), mi);
                i++;
            }else if (nums[mi] < median){
                swap(nums, mi, map(right--, n));
            }else{
                i++;
            }
        }
    }

    private int map(int i, int n) {
        return (1 + 2 * i) % (n | 1);
    }

    private int kth(int[] nums, int k){
        int n = nums.length;
        int l = 0;
        int r = n - 1;
        k--;

        while (l<=r){
            int p = partition(nums, l, r);
            if(p==k) return nums[p];
            if (p < k) l = p + 1;
            else r = p - 1;
        }
        return -1;
    }
    private int partition(int[] a, int l, int r){
        int pivot = a[r];
        int i = l;
        for (int j = l ; j < r ; j++){
            if (a[j] <= pivot){
                swap(a, i++, j);
            }
        }
        swap(a,i,r);
        return i;
    }
    private void swap(int[] a, int i , int j){
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}
