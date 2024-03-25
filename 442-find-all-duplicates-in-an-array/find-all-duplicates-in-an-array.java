class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        boolean[] arr = new boolean[nums.length+1];
        List<Integer> arr_dup = new ArrayList<Integer>();
        for(int i:nums){
            if(arr[i]==false){
                arr[i] = true;
        }else{
            arr_dup.add(i);        
            }
        }
        return arr_dup;
    }
}