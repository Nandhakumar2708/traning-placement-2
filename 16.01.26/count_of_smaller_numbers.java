class Solution {
    int res[];
    int idx[];
    void merge(int nums[],int l,int m,int r){
        int lsize=m-l+1;
        int rsize=r-m;
        int left[]=new int[lsize];
        int right[]=new int[rsize];
        int leftindex[]=new int[lsize];
        int rightindex[]=new int[rsize];
        for(int i=0;i<lsize;i++){
            left[i]=nums[l+i];
            leftindex[i]=idx[i+l];
        }
         for(int i=0;i<rsize;i++){
            right[i]=nums[m+i+1];
            rightindex[i]=idx[i+m+1];
        }
        int j=0;
        for(int i=0;i<lsize;i++){
            while(j<rsize && left[i]>right[j])j++;
            res[leftindex[i]]+=j;
        }
        int lx=0; int rx=0; int index=l;
        while(lx<lsize && rx<rsize){
            if(left[lx]<=right[rx]){
                nums[index]=left[lx];
                idx[index++]=leftindex[lx++];
            }
            else{
                nums[index]=right[rx];
                idx[index++]=rightindex[rx++];
            }
        }
        while(lx<lsize){
            nums[index]=left[lx];
            idx[index++]=leftindex[lx++];
        }
        while(rx<rsize){
            nums[index]=right[rx];
            idx[index++]=rightindex[rx++];
        }
    }
    void mergesort(int nums[],int l,int r){
        if(l==r) return;
        int mid=(l+r)/2;
        mergesort(nums,l,mid);
        mergesort(nums,mid+1,r);
        merge(nums,l,mid,r);
    }
    public List<Integer> countSmaller(int[] nums) {
        int n=nums.length;
        idx=new int[n];
        res=new int[n];
        for(int i=0;i<n;i++)idx[i]=i;
        mergesort(nums,0,n-1);
        List<Integer> ans=new ArrayList<>();
        for(int i:res){
            ans.add(i);
        }
        return ans;
    }
}
