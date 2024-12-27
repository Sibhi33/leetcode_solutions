class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int maxScore = 0;
        int maxI = values[0]; // Initialize with values[0] + 0

        for (int j = 1; j < values.size(); j++) {
            // Calculate the score for the current pair (i, j)
            maxScore = max(maxScore, maxI + values[j] - j);
            // Update maxI to include the current value and index
            maxI = max(maxI, values[j] + j);
        }

        return maxScore;
    }
};
