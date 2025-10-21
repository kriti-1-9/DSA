#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 4, 1, 2, 1, 3, 2};
    int max_val = arr[0];
    for (int i = 1; i < sizeof(arr)/sizeof(arr[0]); i++) {
        if (arr[i] > max_val) {
            max_val = arr[i];
        }
    } 
    int count[max_val + 1] = {0};
    int result[sizeof(arr)]; 
    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
        count[arr[i]]++;
    }
    for(int i=0; i<=max_val; i++) {
        count[i] += count[i-1];
    }
    for (int i = sizeof(arr)/sizeof(arr[0]) - 1; i >= 0; i--) {
        result[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }
    for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
        cout << result[i] << " ";
    }
}