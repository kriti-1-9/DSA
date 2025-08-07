#include <iostream>
#include <vector>
#include <climits>
using namespace std;

bool isPossible(vector<int> &arr, int n, int m, int mid) {
    int painters = 1, time = 0;
    for(int i=0; i<n; i++) {
        if(time + arr[i] <= mid) {
            time += arr[i];
        }
        else {
            painters++;
            time = arr[i];
        }
    }
    return painters <= m;
}
int mintimeTopaint(vector<int> &arr, int n, int m) {
    int sum = 0, maxValue = INT_MIN;
    for(int i=0; i<n; i++) {
        sum += arr[i];
        maxValue = max(maxValue, arr[i]);
    }
    int st = maxValue, end = sum, ans = -1;
    while(st <= end) {
        int mid = st + (end - st) / 2;
        if(isPossible(arr, n, m, mid)) {
            ans = mid;
            end = mid - 1;
        }
        else {
            st = mid + 1;
        }
    }
    return ans;
}
int main(){
    vector<int> arr={40, 30, 10, 20};
    int n = 4, m = 2;
    cout << mintimeTopaint(arr, n, m) << endl;
    return 0;
}