#include<iostream>
using namespace std;

int binToDecimal(int bin) {
	int ans = 0, pow = 1;
	while(bin > 0) {
		int rem = bin % 10;
		ans += rem * pow;
		
		bin /= 10;
		pow *= 2;
	}
	return ans;
}

int dec_to_bin(int dec_num){
	int ans = 0, pow = 1;
	while(dec_num > 0) {
		int rem = dec_num % 2;
		dec_num /= 2;
		ans += (rem*pow);
		pow *= 10;
	}
	return ans;
}

int main(){
	int dec_num;

	// cin >> dec_num;
	// cout << dec_to_bin(dec_num) << endl;

	cout << binToDecimal(100) << endl;

	return 0;
}
