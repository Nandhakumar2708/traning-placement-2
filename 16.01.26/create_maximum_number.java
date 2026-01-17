class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        int n1 = nums1.length, n2 = nums2.length, l2;
        int[] ans= new int[k];
        for(int l1=Math.max(0, k-n2); l1<=Math.min(k, n1); l1++) {
            l2 = k-l1;
            int[] t1 = getMaxm(nums1, l1);
            int[] t2 = getMaxm(nums2, l2);
            int[] t = merge(t1, t2, k);
            if(isGreater(t, 0, ans, 0)) {
                ans = t;
            }
        }
        return ans;
    }

    private int[] getMaxm(int[] arr, int l) {
        if (l == 0) return new int[0];
        Deque<Integer> deque = new LinkedList<>();
        int toRemove = arr.length - l;
        for(int i=0; i<arr.length; i++) {
            while(!deque.isEmpty() && deque.peekLast()<arr[i] && toRemove>0) {
                deque.removeLast();
                toRemove--;
            }
            deque.add(arr[i]);
        }
        int[] res = new int[l];
        for(int i=0; i<l; i++) {
            int p = deque.removeFirst();
            res[i] = p;
        }
        return res;
    }

    private int[] merge(int[] t1, int[] t2, int size) {
        int[] res = new int[size];
        int i=0, j=0, k=0;
        while(k < size) {
            if(isGreater(t1, i, t2, j)) {
                res[k++] = t1[i++];
            } else {
                res[k++] = t2[j++];
            }
        }
        return res;
    }

    private boolean isGreater(int[] t1, int i, int[] t2, int j) {
        while(i < t1.length && j < t2.length) {
            if(t1[i] != t2[j])
                return t1[i] > t2[j];
            i++;
            j++;
        }
        return i < t1.length;
    }
}
