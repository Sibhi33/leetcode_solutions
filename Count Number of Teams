class Solution {
public:
    static int  numTeams(vector<int>& rating) {
        const int n = rating.size();
        int cnt= 0;
        for (int i= 1; i < n-1; i++) {
            int L[2]={0}, R[2]={0};

            // Count ratings on the left of i
            for (int j = 0; j < i; j++) 
                L[rating[j] < rating[i]]++;//rating is unique
            
            // Count ratings on the right of i
            for (int k=i+1; k<n; k++) 
                R[rating[k] < rating[i]]++;

            // number of valid teams
            cnt += L[0]*R[1] + L[1]*R[0];
        }
        return cnt;
    }
};




auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();
