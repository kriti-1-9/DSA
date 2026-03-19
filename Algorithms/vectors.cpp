#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> vec; // Initialize an empty vector
    cout<<"size="<<vec.size()<<endl;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);
    cout<<"after push back size="<<vec.size()<<endl;
    vec.pop_back();
    cout<<vec.front()<<endl;
    cout<<vec.back()<<endl;

    cout<<vec.at(1)<<endl;
    cout<<vec.capacity()<<endl;
    /*for(char val: vec){
        cout<<val<<endl;
    }*/
    
    //vector<int> vec(5,0);
    //for(int i:vec){
    //   cout<<i<<endl;
    //}
	//cout<<vec[0]<<endl;
	//vector<char> vec1;

    /*vector<char> vec={'a','b','c','d','e'};//3
    cout <<"size="<<vec.size()<<endl;
    for(char val: vec){
        cout<<val<<endl;
    }*/
	return 0;
}
