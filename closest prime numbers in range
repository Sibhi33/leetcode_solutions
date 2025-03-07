class Solution {
    private static final int N = 1000002;
    private boolean[] prime = new boolean[N];

    public Solution() {
        seive();
    }

    private void seive() {
        for (int i = 0; i < N; i++) prime[i] = true;
        prime[0] = prime[1] = false;

        for (int i = 2; i * i < N; i++) {
            if (prime[i]) {
                for (int j = i * i; j < N; j += i) {
                    prime[j] = false;
                }
            }
        }
    }

    public int[] closestPrimes(int left, int right) {
        int prev = -1, diff = Integer.MAX_VALUE;
        int[] ans = {-1, -1};

        for (int i = left; i <= right; i++) {
            if (prime[i]) {
                if (prev != -1 && i - prev < diff) {
                    ans[0] = prev;
                    ans[1] = i;
                    diff = i - prev;
                }
                prev = i;
            }
        }
        return ans;
    }
}
