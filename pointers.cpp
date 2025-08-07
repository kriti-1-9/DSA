#include<iostream>
#include<vector>
using namespace std;

void changeA(int &b){//pass by reference using alias
    b=20;
}

// void changeA(int* ptr){//pass by reference using pointers
//     *ptr=20;
// }

// void changeA(int a){//pass by value
//     a=20;
// }

int main(){
    int a=10;
    changeA(a);
    cout<<"inside main function:"<<a<<endl;//20

    // changeA(&a);
    // cout<<"inside main function:"<<a<<endl;//20

    // changeA(a);
    // cout<<"inside main function:"<<a<<endl;//20

    // int* ptr=&a;
    // int** parptr=&ptr;
    // cout<<*(parptr)<<endl;
    // cout<<*(ptr)<<endl;
    // cout<<**(parptr)<<endl;

    // cout<<*(&a)<<endl;
    // cout<<*(ptr)<<endl;

    // int** parptr=&ptr;
    // cout<<&ptr<<endl;
    // cout<<parptr<<endl;

    // float price=100.25f;
    // float *ptr=&price;
    // cout<<ptr<<endl;
    // cout<<&price<<endl;
    return 0;
}