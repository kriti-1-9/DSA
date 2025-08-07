#include<iostream>
using namespace std;
void reverse_array(int arr[], int size){
	int start=0, end=size-1;
	while(start<end){
		swap(arr[start],arr[end]);
		start++;
		end--;
	}
}
int main(){
	//+infinity=INT_MAX in c++
	//minimun=min(num[i],smallest);
	int arr[]={2,4,5,6,3,9,99};
	int size=7;
	reverse_array(arr,size);
	for(int i=0;i<7;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
}
