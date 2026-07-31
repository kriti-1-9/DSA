class Solution {
public:
    void solve(vector<string>& ans,vector<string>& words,int i,int maxwidht){
        int n=words.size();
        if(i>=n){
            return ;
        }
        queue<string> q;
        int lenused=0;
        int curri=i;
        for(int ind=i;ind<n;ind++){
           if(lenused+words[ind].size()+(ind-i)<=maxwidht){
            curri=ind;
            q.push(words[ind]);
            lenused+=words[ind].size();
            // lenused++;
           }   
           else{
            break;
           }
        }
        int spaces=maxwidht-lenused;
        string word="";
        if(curri==n-1){
           while(!q.empty()){
                word+=q.front();
                q.pop();
                if(!q.empty())
                word+=" ";
            }
            while(word.size()<maxwidht){
                word+=" ";
            }
        }
        else{
            //if 3words and 6 spaces  6/(3-1)=3   6%(3-1)=0
            //if 3 words and 7 spaces  7/(3-1)=3  7%(3-1)=1
            //if 4words and 6 spaces   6/(4-1)=3   6%(4-1)=2
            int nq=q.size();
            if(nq==0){
                return;
            }
            if(nq==1){
             word=q.front();
             while(word.size()<maxwidht)
               word+=" ";
                ans.push_back(word);
                solve(ans,words,curri+1,maxwidht);
                return;
            }
            int betweenEach=spaces/(nq-1);
            int leftOver=spaces%(nq-1);
            while(!q.empty()){
                word+=q.front();
                q.pop();
                if(!q.empty()){
                    int cnt=betweenEach;
                    if(leftOver>0){
                        cnt++;
                        leftOver--;
                    }
                    for(int space=0;space<cnt;space++){
                        word+=" ";
                    }
                }
            }
        }
        ans.push_back(word);
        solve(ans,words,curri+1,maxwidht);
    }
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ans;
        solve(ans,words,0,maxWidth);
        return ans;
    }
};