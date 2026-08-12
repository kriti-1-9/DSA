#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> result;
        
        // Loop through all possible hours
        for (int h = 0; h < 12; h++) {
            // Loop through all possible minutes
            for (int m = 0; m < 60; m++) {
                // Check if the sum of set bits in h and m matches turnedOn
                if (__builtin_popcount(h) + __builtin_popcount(m) == turnedOn) {
                    
                    // Format the string:
                    // Hour has no leading zero.
                    // Minutes must have two digits (use a ternary or printf style).
                    string time = to_string(h) + ":" + (m < 10 ? "0" : "") + to_string(m);
                    result.push_back(time);
                }
            }
        }
        
        return result;
    }
};