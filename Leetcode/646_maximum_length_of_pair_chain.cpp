class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        int n = pairs.size();
        sort(pairs.begin(), pairs.end(), [](auto&a, auto&b){
            return a[1]<b[1];
        });

        int ans =1;
        int idx=0;
        for(int i=1; i<n;i++){
            if(pairs[i][0]>pairs[idx][1]){
                ans++;
                idx = i;
            }
        }
        return ans;
        
    }
};