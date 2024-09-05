class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int m = rolls.size();
        int rollSum = mean * (m + n);
        for (auto& rollVal : rolls) {
            rollSum -= rollVal;
        }
        if (rollSum < 0) return {};
        int faceVal = rollSum / n;
        int facesGettingExtra = rollSum % n;
        if (faceVal == 0 || faceVal + (facesGettingExtra > 0 ? 1 : 0) > 6) return {};
        vector<int> nRolls(n);
        for (int indx = 0; indx < n; indx++) {
            nRolls[indx] = faceVal;
            if (facesGettingExtra-- > 0) nRolls[indx]++;
        }
        return nRolls;
    }
};
