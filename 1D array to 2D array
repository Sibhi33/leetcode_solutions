class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& arr1D, int rows, int cols) {
        // Initialize a 2D vector with 'rows' number of rows and 'cols' number of columns
        vector<vector<int>> arr2D(rows, vector<int>(cols));

        // Check if the total elements in the 1D array match the required elements in the 2D array
        if (rows * cols != arr1D.size()) {
            return {};  // Return an empty vector if the dimensions don't match
        }

        // Fill the 2D array with elements from the 1D array
        for (int i = 0; i < rows; i++) {        
            for (int j = 0; j < cols; j++) {    
                // Calculate the correct index in the 1D array and assign the value to the 2D array
                arr2D[i][j] = arr1D[i * cols + j];
            }
        }

        
        return arr2D;
    }
};
