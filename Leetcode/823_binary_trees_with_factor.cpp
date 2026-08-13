class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        unordered_map<long, long> dp;
        long mod = 1e9 + 7;
        long totalTrees = 0;

        for (int i = 0; i < arr.size(); i++) {
            // Every number can at least form a single-node tree
            dp[arr[i]] = 1;

            // Check all smaller numbers as potential left children
            for (int j = 0; j < i; j++) {
                // If arr[j] is a factor of arr[i]
                if (arr[i] % arr[j] == 0) {
                    int factor1 = arr[j];
                    int factor2 = arr[i] / arr[j];

                    // Check if the corresponding right child exists in the array
                    if (dp.count(factor2)) {
                        // Combinations = (Trees from left child) * (Trees from right child)
                        dp[arr[i]] = (dp[arr[i]] + dp[factor1] * dp[factor2]) % mod;
                    }
                }
            }
            totalTrees = (totalTrees + dp[arr[i]]) % mod;
        }

        return (int)totalTrees;
    }
};