string eng[] =      { "",        "One",       "Two",      "Three",
                      "Four",    "Five",      "Six",      "Seven",
                      "Eight",   "Nine",      "Ten",      "Eleven",
                      "Twelve",  "Thirteen",  "Fourteen", "Fifteen",
                      "Sixteen", "Seventeen", "Eighteen", "Nineteen"};

string eng2[] =     {  "",      "Ten",   "Twenty",  "Thirty", "Forty",
                       "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

string eng3[] = {"", "Thousand", "Million", "Billion"};

class Solution {
public:
    static string toEnglish(int num) {
        string ans = "";

        if (num >= 100) {
            auto [q, r] = div(num, 100);
            ans += eng[q] + " Hundred ";
            num = r;
        }

        if (num >= 20) {
            auto [q2, r2] = div(num, 10);
            ans += eng2[q2];
            if (r2 > 0)
                ans += " " + eng[r2];
        } else if (num > 0)
            ans += eng[num];

        // Trim trailing space
        if (!ans.empty() && ans.back() == ' ')
            ans.pop_back();
        return ans;
    }

    static string numberToWords(int num) {
        if (num == 0)
            return "Zero";

        string ans = "";
        int count = 0;

        while (num > 0) {
            auto [q, r] = div(num, 1000);
            num = q;

            if (r > 0) {
                string part = toEnglish(r) + " " + eng3[count];
                ans = (ans.empty()) ? part : part + " " + ans;
            }
            count++;
        }
        // Trim trailing space
        if (!ans.empty() && ans.back() == ' ') {
            ans.pop_back();
        }
        return ans;
    }
};
