class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        int maxSize = 0;

        // Iterate through each bit position (assuming 32-bit integers)
        for (int bit = 0; bit < 32; ++bit) {
            int count = 0;

            // Count how many numbers have this bit set
            for (int num : candidates) {
                if (num & (1 << bit)) {
                    count++;
                }
            }

            // Update maxSize with the maximum count for any bit position
            maxSize = max(maxSize, count);
        }

        return maxSize;
    }
};
