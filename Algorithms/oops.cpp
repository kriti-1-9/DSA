#include <iostream>
#include <string>
using namespace std;

// class Teacher {
// private:
//     double salary;
// public:
// //non parameterized constructor
//     Teacher(){//same naam ke constructor ho sakte hai bt parameters ya unke type different hone chahiye : constructor overloading, an example of polymorphism
//         dept = "Computer Science";
//         // cout << "HI, I an constructor.\n";
//     }

//     //parameterized constructor
//     Teacher(string name, string dept, string s, double sal){
//         this->name = name;
//         this->dept = dept;
//         subject = s;
//         salary = sal;
//     }

//     //copy constructor
//     Teacher(Teacher &orgObj) { //pass by reference
//         cout << "i am custom copy constructor" << endl;
//         this->name = orgObj.name;
//         this->dept = orgObj.dept;
//         this->subject = orgObj.subject;
//         this->salary = orgObj.salary;
//     }

//     //properties/attributes
//     string name;
//     string dept;
//     string subject;

//     //methods / member functions
//     void changeDept(string newDept) {
//         dept = newDept;
//     };

//     void getInfo(){
//         cout << "name: " << name << endl;
//         cout << "subject: " << subject << endl;
//     }

//     //setter
//     // void setSalary(double s) {
//     //     salary = s;
//     // }
//     // //getter
//     // double getSalary() {
//     //     return salary;
//     // }
// };

// class Account {
// private:
//     double balance;
//     string password;  //data hiding
// public:
//     string accountId;
//     string username;
// };

class Student {
public:
    string name;
    // double cgpa;
    double* cgpaPtr;
    // int rollno;
    // int age;
    Student(string name, double cgpa) {
        this->name = name;
        cgpaPtr = new double;
        *cgpaPtr = cgpa;
    }
    
    Student(Student &obj) {
        this->name = obj.name;
        cgpaPtr = new double;
        *cgpaPtr = *obj.cgpaPtr;
        // this->cgpa = obj.cgpa;
        // this->cgpaPtr = obj.cgpaPtr;
    }

    //destructor
    ~Student(){//same name as class
        cout << "Hi, I delete everything." << endl;
    }

    void getInfo() {
        cout << "name: " << name << endl;
        // cout << "cgpa: " << cgpa << endl;
        cout << "cgpa: " << *cgpaPtr << endl;
    }
};

int main() {
    Student s1("Kriti", 8);
    s1.getInfo();

    // s1.getInfo();
    // Student s2(s1);
    // *(s2.cgpaPtr) = 9.2;
    // //s1 wala ptr bhi change ho jaega;
    // s1.getInfo();
    // s2.getInfo();

    // Teacher t1("Kriti", "Computer Science", "C++", 25000);
    // t1.getInfo();
    // Teacher t2(t1); //custom copy constructor -invoke
    // t2.getInfo();

    // Teacher t1;//Constructor call

    // t1.name = "Kriti";
    // t1.subject = "C++";
    // t1.dept = "Computer Science";
    // t1.salary = 25000;
    // t1.setSalary(25000);

    // cout << t1.name << endl;
    // cout << t1.getSalary() << endl;
    // cout << t1.dept << endl;

    // Teacher t2;
    // Teacher t3;
    // Teacher t4;
    return 0;
}