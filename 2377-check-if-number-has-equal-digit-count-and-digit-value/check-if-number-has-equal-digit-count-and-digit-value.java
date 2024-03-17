import java.util.*;
class Solution {
    public boolean digitCount(String num) {
        String[] splitArray = num.split("");
        int[] arr = new int[splitArray.length];
        for(int i = 0;i<splitArray.length;i++){
            arr[i] = Integer.parseInt(splitArray[i]);
        }
        Map<Integer,Integer> map = new HashMap<>();
        
        for(int i = 0;i<arr.length;i++){
            int count = 0;
            if(!(map.containsKey(i))){
                for(int j=0;j<arr.length;j++){
                    if(arr[j]==i){
                        count++;
                    }
                }
                map.put(i,count);
            }
        }
        Collection<Integer> values = map.values();
        int[] valueArray = new int[values.size()];
        int k = 0;
        for(int item:values){
            valueArray[k++] = item;
        }
        return Arrays.equals(arr,valueArray);
    }
}