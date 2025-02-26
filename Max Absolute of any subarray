class Solution {
    public int maxAbsoluteSum(int[] nums) {
        int n = nums.length;
        int maxEndingHere = nums[0];
        int minEndingHere = nums[0];
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        
        // Kadane's algorithm to find max and min subarray sums
        for (int i = 1; i < n; i++) {
            maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]);
            minEndingHere = Math.min(nums[i], minEndingHere + nums[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
            minSoFar = Math.min(minSoFar, minEndingHere);
        }
        
        // The maximum absolute sum is the maximum of the absolute values of maxSoFar and minSoFar
        return Math.max(Math.abs(maxSoFar), Math.abs(minSoFar));
    }
}
