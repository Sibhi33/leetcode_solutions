class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int n = rowSum.length;
        int m = colSum.length;
        int [][]matrix = new int[n][m];
        for(int i = 0; i < n; i ++){
            for(int j = 0; j < m; j ++){
                if(rowSum[i] < colSum[j]){
                    matrix[i][j] = rowSum[i];
                }
                else if(rowSum[i] > colSum[j]){
                    matrix[i][j] = colSum[j];
                }
                else{
                    matrix[i][j] = colSum[j];
                }
                rowSum[i] -= matrix[i][j];
                colSum[j] -= matrix[i][j];
            }
        }
        return matrix;
    }
}
