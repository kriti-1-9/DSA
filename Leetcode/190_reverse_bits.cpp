class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        for (int i = 0; i < 32; i++) {
            // 1. Shift result to the left to make room for the new bit
            result <<= 1;
            
            // 2. If the current bit of n is 1, add 1 to result
            // (n & 1) extracts the rightmost bit
            if (n & 1) {
                result++;
            }
            
            // 3. Shift n to the right to process the next bit
            n >>= 1;
        }
        return result;
    }
};