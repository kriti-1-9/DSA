class Solution {
public:
    bool vowels(char ch) {
        vector<char> vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        for(char val: vowel) {
            if(ch == val) {
                return true;
            }
        }
        return false;
    } 
    string reverseVowels(string s) {
        int st = 0;
        int end = s.size()-1;
        while(end > st) {
            if(vowels(s[st]) && vowels(s[end])) {
                char t = s[st];
                s[st] = s[end];
                s[end] = t;
                st++;
                end--;
            }
            else if(vowels(s[st]) && !vowels(s[end])) {
                end--;
            }
            else if(!vowels(s[st]) && vowels(s[end])) {
                st++;
            }
            else {
                st++;
                end--;
            }
        }
        return s;
    }
};