class Solution {
    public int[] searchRange(int[] nums, int target) {
        
        int i = binSearchleft(nums,target);
        int j = binSearchright(nums,target);
        int[] arr = {-1,-1};
        if(i<=j){
            arr[0] = i;
            arr[1] = j;
        }
        return arr;
    }
    public int binSearchleft(int[] nums,int target){
        int start = 0;
        int end = nums.length-1;
        while(start<=end){
            int mid = (start+end)/2;
            if(target>nums[mid]){
                start = mid+1;
            }
            else{
                end = mid-1;
            }
        }
        return start;
    }
    public int binSearchright(int[] nums,int target){
        int start = 0;
        int end = nums.length-1;
        while(start<=end){
            int mid = (start+end)/2;
            if(nums[mid]<=target){
                start = mid+1;
            }
            else{
                end = mid-1;
            }
        }
        return end;
    }

}