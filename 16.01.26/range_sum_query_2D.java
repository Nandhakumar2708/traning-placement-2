class NumMatrix {

    private int[][] m;

    public NumMatrix(int[][] matrix) {
        m = new int[matrix.length][matrix[0].length];
        m[0][0] = matrix[0][0];
        for (int i = 1; i < matrix[0].length; i++) {
            m[0][i] = matrix[0][i] + m[0][i - 1];
        }
        for (int i = 1; i < matrix.length; i++) {
            m[i][0] = matrix[i][0] + m[i - 1][0];
        }
        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                m[i][j] = matrix[i][j] + m[i][j - 1] + m[i - 1][j] - m[i - 1][j - 1];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int result = m[row2][col2];
        if (row1 > 0) {
            result -= m[row1 - 1][col2];
        }
        if (col1 > 0) {
            result -= m[row2][col1 - 1];
        }
        if (row1 > 0 && col1 > 0) {
            result += m[row1 - 1][col1 - 1];
        }
        return result;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
