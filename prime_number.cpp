#include <iostream>
using namespace std;

//sieve of eratosthenes->leetcode problem 204

string isPrime(int n) {
    for(int i=2; i*i <=n; i++) {
        if(n % i == 0) {
            return "Non prime";
        }
    }
    return "Prime";
}

int main() {
    int n = 41;
    cout << isPrime(n) <<endl;
    return 0;
}