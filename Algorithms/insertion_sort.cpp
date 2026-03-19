#include<iostream>
using namespace std;

// time complexity = O(n), O(n^2), O(n^2)
// space complexity = 1
// stable algorithm

void insertionsort(int arr[], int n) {
    for(int i=1; i<n; i++) {
        int curr = arr[i];
        int prev = i-1;
        while(prev >=0 && arr[prev] > curr) {
            arr[prev+1] = arr[prev];
            prev--;
        }
        printArray(arr, i);
        arr[prev+1] = curr;
    }
}

void printArray(int arr[], int n) {
    for(int i=0; i<n; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
   int n = 5;
   int arr[] = {56, 89, 66, 10, 32};
   insertionsort(arr, n);
   return 0;
}