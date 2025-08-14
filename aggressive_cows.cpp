#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool isPossible(vector<int> &arr, int N, int C, int minAllowedDist) {
    //sort in getDistance
    int cow = 1, lastStallPos = arr[0];

    for(int i=1; i<N; i++) {
        if(arr[i]-lastStallPos >= minAllowedDist) {
            cow++;
            lastStallPos = arr[i];
        }
        if(cow == C) {
            return true;
        }
    }
    return false;
} 

int getDistance(vector<int> &arr, int N, int C) {
    sort(arr.begin(), arr.end()); // NlogN
    //st = 1, end = maxValue - minvalue;
    int st = 1, end = arr[N-1] - arr[0], ans = -1;
    while(st <= end) { // O(log(range) * N)
        int mid = st + (end -st) / 2;
        if(isPossible(arr, N, C, mid)) { // right
            ans = mid;
            st = mid + 1;
        } else { // left
            end = mid - 1;
        }
    } 
    return ans;
}

int main() {
    int N = 5, C=3;
    vector<int> arr = {1, 2, 8, 4, 9};

    cout << getDistance(arr, N, C) << endl;
    return 0;
}