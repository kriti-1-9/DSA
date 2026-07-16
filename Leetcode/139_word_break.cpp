class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.size();
        vector<bool> dp(n+1, 0);
        dp[0] = 1;
        for(int i=1; i<=n; i++) {
            for(string &w: wordDict) {
                int start = i-w.size();
                if(start >= 0 && dp[start] && s.substr(start, w.size()) == w) {
                    dp[i] = 1; break;
                }
            }
        }
        return dp[n];
    }
};