class Solution {
    public int maxScore(String s) {
        int totalZeros = 0;
        for (char c : s.toCharArray()) {
            if (c == '0') totalZeros++;
        }
        int ans = -1, zeros = 0, n = s.length();
        for (int i = 1; i < n; i++) {
            if (s.charAt(i - 1) == '0') {
                zeros++;
                totalZeros--;
            }
            ans = Math.max(ans, zeros + (n - totalZeros - i));
        }
        return ans;
    }
}
