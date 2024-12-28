class Solution {
    public int[] maxSumOfThreeSubarrays(int[] nums, int k) {
        // Total possible subarrays of length k
        int n = nums.length - k + 1;

        // Array to store the sum of all subarrays of length k
        int[] sums = new int[n];
        int windowSum = 0;

        // Calculate the sum of the first subarray of length k
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }
        sums[0] = windowSum;

        // Calculate the sum of remaining subarrays using a sliding window approach
        for (int i = k; i < nums.length; i++) {
            windowSum = windowSum - nums[i - k] + nums[i];
            sums[i - k + 1] = windowSum;
        }

        // DP memoization table to store results for subproblems
        int[][] memo = new int[n][4];
        for (int[] row : memo) {
            Arrays.fill(row, -1); // Initialize with -1 (indicating not calculated yet)
        }

        // List to store the indices of the optimal subarrays
        List<Integer> indices = new ArrayList<>();

        // Use DP to calculate the maximum sum of three non-overlapping subarrays
        dp(sums, k, 0, 3, memo);

        // Reconstruct the indices of the selected subarrays
        dfs(sums, k, 0, 3, memo, indices);

        // Convert the indices list to an array for the result
        int[] result = new int[3];
        for (int i = 0; i < 3; i++) {
            result[i] = indices.get(i);
        }

        return result;
    }

    // DP function to calculate the maximum sum using memoization
    private int dp(int[] sums, int k, int idx, int rem, int[][] memo) {
        // Base case: If no subarrays left to pick, return 0
        if (rem == 0) return 0;

        // Base case: If the index goes out of bounds, return a very low value
        if (idx >= sums.length) {
            return (rem > 0) ? Integer.MIN_VALUE : 0;
        }

        // If the result is already computed, return it
        if (memo[idx][rem] != -1) {
            return memo[idx][rem];
        }

        // Option 1: Include the current subarray and move k steps forward
        int include = sums[idx] + dp(sums, k, idx + k, rem - 1, memo);

        // Option 2: Skip the current subarray and move to the next index
        int exclude = dp(sums, k, idx + 1, rem, memo);

        // Store the maximum of include and exclude in the memoization table
        return memo[idx][rem] = Math.max(include, exclude);
    }

    // DFS function to reconstruct the indices of the chosen subarrays
    private void dfs(int[] sums, int k, int idx, int rem, int[][] memo, List<Integer> indices) {
        // Base case: If no subarrays left to pick, return
        if (rem == 0) return;

        // Base case: If the index goes out of bounds, return
        if (idx >= sums.length) return;

        // Compute the "include" and "exclude" options to determine the path
        int include = sums[idx] + dp(sums, k, idx + k, rem - 1, memo);
        int exclude = dp(sums, k, idx + 1, rem, memo);

        // If including the current subarray is optimal, add its index and move forward
        if (include >= exclude) {
            indices.add(idx);
            dfs(sums, k, idx + k, rem - 1, memo, indices);
        } else {
            // Otherwise, skip the current subarray and move to the next index
            dfs(sums, k, idx + 1, rem, memo, indices);
        }
    }
}
