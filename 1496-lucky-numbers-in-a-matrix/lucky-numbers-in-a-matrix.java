class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        int[] row_min = new int[matrix.length];
        int[] col_max = new int[matrix[0].length];
        // int[] res = new int[matrix.length];
        for(int i=0;i<matrix.length;i++){
            int min = matrix[i][0];
            for(int j=0;j<matrix[i].length;j++){
                if(matrix[i][j]<=min){
                    min = matrix[i][j];
                }
            }
            row_min[i] = min;
        }
        for(int k=0;k<matrix[0].length;k++){
            int max = 0;
            for(int l=0;l<matrix.length;l++){
                if(matrix[l][k]>max){
                    max = matrix[l][k];
                }
            }
            col_max[k] = max;
        }
        if(col_max.length>row_min.length){
            List<Integer> res = new ArrayList<Integer>();
            for(int p=0;p<col_max.length;p++){
                for(int q=0;q<row_min.length;q++){
                    if(col_max[p]==row_min[q]){
                        res.add(row_min[q]);
                    }
                }
            }
            return res;
        }
        else{
            List<Integer> res = new ArrayList<Integer>();
            for(int p=0;p<row_min.length;p++){
                for(int q=0;q<col_max.length;q++){
                    if(row_min[p]==col_max[q]){
                        res.add(col_max[q]);
                    }
                }
            }
            return res;
        }
    }
}