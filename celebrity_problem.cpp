// Given a 2D array (n X n), such that arr[i][j] = 1 means its person knows ith person, the task is to find the celebrity.
// A celebrity is defined as someone who is known to all but does not know anyone.
// Return the index of the celebrity, if there is no celebrity return -1.

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int getCelebrity(vector<vector<int>>& arr) {
    int n = arr.size();
    stack<int> s;
    for (int i = 0; i < n; i++) {
        s.push(i);
    }

    while (s.size() > 1) {
        int i = s.top();
        s.pop();

        int j = s.top();
        s.pop();

        if(arr[i][j] == 0) {
            s.push(i);
        } else {
            s.push(j);
        }
    }
    int celeb = s.top();
    for (int i = 0; i < n; i++) {
        if (i != celeb) {
            if (arr[celeb][i] == 1 || arr[i][celeb] == 0) {
                return -1;
            }
        }
    }
    return celeb;
}

int main() {
    vector<vector<int>> arr = {
        {0, 1, 0},
        {0, 0, 0},
        {0, 1, 0}
    };
    int ans = getCelebrity(arr);
    cout << "Celebrity is": << ans << endl;
    return 0;
}