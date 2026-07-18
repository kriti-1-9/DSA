class Solution {
public:
    int GCD(int a, int b) {
        if(b == 0) return a;
        if(b > a) {
            int temp = b;
            b = a;
            a = temp;
        }
        return gcd(a, b);
    }

    int findGCD(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        return gcd(nums[0], nums[nums.size() - 1]);    
    }
};