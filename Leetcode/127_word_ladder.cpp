class Solution {
public:
    int ladderLength(string s, string e, vector<string>& word) {
        unordered_set<string> st(word.begin(), word.end());
        int res = 0;
        int m = s.length();
        queue<string> q;
        q.push(s);
        while(!q.empty()) {
            res++;
            int len = q.size();
            for(int i=0; i<len; ++i) {
                string word = q.front();
                q.pop();
                for(int j=0; j<m; ++j) {
                    char ch = word[j];
                    for(char c = 'a'; c<='z'; ++c) {
                        word[j] = c;
                        if(st.find(word) == st.end()) continue;
                        if(word == e) return res+1;
                        st.erase(word);
                        q.push(word);
                    }
                    word[j] = ch;
                }
            }
        }
        return 0;
    }
};