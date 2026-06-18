class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1 || s.size() < numRows) return s;
        vector<string> rows(numRows);
        int currentRow = 0;
        bool down = false;
        for(char c : s) {
            rows[currentRow] += c;
            if(currentRow == 0 || currentRow == numRows-1) down = !down;
            currentRow += down ? 1 : -1;
        }
        string result;
        for(auto row : rows) {
            result += row;
        }
        return result;
    }
};