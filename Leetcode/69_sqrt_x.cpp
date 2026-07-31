class Solution {
public:
    int mySqrt(int x) {
        for (long int i=0; i<=x; i++) {
            if (i*i > x) {
                return i-1;
            }
            if (i*i == x) {
                return i;
            }
        }
        return -1;
    }
};