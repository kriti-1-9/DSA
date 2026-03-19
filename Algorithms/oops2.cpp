// friend function and friend class => explore



// Static Keyword
// Static Variables
// Variables declared as static in a function are created & initialised once for the lifetime of the program. // in function
// Static variables in a class are created & initialised once. They are shared by all the objects of the class. // in class
// Static Objects

#include <iostream>
#include <string>
using namespace std;

class ABC {
public:
    ABC() {
        cout << "constructor\n";
    }
    ~ABC() {
        cout << "destruction\n";
    }
};

int main() {
    if(true) {
        static ABC obj;
        // ABC obj;
    }
    cout << "end of main fnx\n";
    return 0;
}

// #include <iostream>
// #include <string>
// using namespace std;


// class A {
// public:
//     int x;
//     void incX() {
//         x = x+1;
//     }
// };

// void fun() {
//     static int x = 0;
//     cout << "x: " << x << endl;
//     x++;
// }

// int main() {
//     A obj1;
//     A obj2;

//     obj1.x = 100;
//     obj2.x = 200;

    // cout << obj1.x << endl;
    // obj1.incX();
    // cout << obj1.x << endl;
    // cout << obj2.x << endl;

    // fun(); //0
    // fun(); //1
    // fun(); //2
//     return 0;
// }




// Abstraction : Hiding all unnecessary details & showing only the important parts.
// using abstract classes
// Abstract classes are used to provide a base class from which other classes can be derived.
// They cannot be instantiated(instance->object) and are meant to be inherited.
//Abstract classes are typically used to defined an interface for derived classes.

// #include <iostream>
// #include <string>
// using namespace std;

// class Shape { // abstract class
//     virtual void draw() = 0; //pure virtual function
// };

// class Circle : public Shape {
// public:
//     void draw() {
//         cout << "drawing a circle\n";
//     }
// };

// int main() {
//     Circle c1;
//     c1.draw();
//     return 0;
// }




// Run Time Polymorphism
// Virtual Functions : A virtual function is a member function that you expect to be redefined in derived classes.
// Virtual functions are dynamic in nature.
// Defined by keyword "virtual" inside a base class and are always declared with a base class and overriden in a child class.
// A vitual function is called during Runtime.
 
// #include <iostream>
// #include <string>
// using namespace std;

// class Parent {
// public:
//     void getInfo() {
//         cout << "parent class\n";
//     }
//     virtual void hello() {
//         cout << "hello from parent\n";
//     }
// };

// class Child : public Parent {
// public:
//     void getInfo() {
//         cout << "child class\n";
//     }
//     void hello() {
//         cout << "hello from child\n";
//     }
// };

// int main() {
//     Child c1;
//     c1.hello();
//     return 0;
// }



// Run time polymorphism
// Function Overriding
// Parent & Child both contain the same function with different implementation. The parent class function is said to be overriden.

// #include <iostream>
// #include <string>
// using namespace std;

// class Parent {
// public:     
//     void getInfo() {
//         cout << "parent class\n";
//     }
// };

// class Child : public Parent {
// public:
//     void getInfo() {
//         cout << "child class\n";
//     }
// };

// int main() {
//     Child c1;
//     c1.getInfo();
//     return 0;
// }



// function overloading

// #include <iostream>
// #include <string>
// using namespace std;

// class Print {
// public:
//     void show(int x) {
//         cout << "int: " << x << endl;
//     }

//     void show(char ch) {
//         cout << "char: " << ch << endl;
//     }
// };

// int main() {
//     Print p1;
//     p1.show('&');
//     return 0;
// }




// Polymorphism: polymorphism is the ability of objects to take on different forms or behave in different ways depeng on the context in which they are used.
// Compile time polymorphism
// Run time Polymorphism
// Many forms




// #include <iostream>
// #include <string>
// using namespace std;

// class Student {
// public:
//     string name;

//     Student() {
//         cout << "non-parameterized\n";
//     }

//     Student(string name) {
//         this->name = name;
//         cout << "parameterized\n";
//     }
// };

// int main() {
//     Student s1("tony stark");
//     return 0;
// }



// hybrid inheritance



// hierarical inheritance
// #include <iostream>
// #include <string>
// using namespace std;

// class Person {
// public:
//     string name;
//     int age;
// };

// class Student : public Person {
// public:
//     int rollno;
// };

// class Teacher : public Person {
// public:
//     string subject;
// };



//multiple inheritance
// #include <iostream>
// #include <string>
// using namespace std;

// class Student {
// public:
//     string name;
//     int rollno;
// };

// class Teacher {
// public:
//     string subject;
//     double salary;
// };

// class TA : public Student, public Teacher {

// };

// int main() {
//     TA t1;
//     t1.name = "tony stark";
//     t1.subject = "engineering";

//     cout << t1.name << endl;
//     cout << t1.subject << endl;

//     return 0;
// }



// #include <iostream>
// #include <string>
// using namespace std;

// class Person {
// public:
//     string name;
//     int age;

//     // Person(string name, int age) {
//     //     this->name = name;
//     //     this->age = age;
//     // }

//     // Person() {
//     //     cout << "parent constructor\n";
//     // }
// };

// class Student : public Person{
// public:
//     int rollno;

//     // Student(string name, int age, int rollno) : Person(name, age){
//     //     this->rollno = rollno;

//     //     // cout << "child construcor\n";
//     // }
    
//     // void getInfo() {
//     //     cout << "name: " << name << endl;
//     //     cout << "age: " << age << endl;
//     //     cout << "rollno: " << rollno << endl;
//     // }
// };

// class GrandStudent : public Student {
// public:
//     string researchArea;
// }

//  int main() {
//     GrandStudent s1;
//     s1.name = "tony stark";
//     s1.researchArea = "quantum physics";
//     cout << s1.name << endl;
//     cout << s1.researchArea << endl;

     // Student s1("Kriti", 21, 1234);
     // s1.getInfo();

     // Student s1;
     // s1.name = "Kriti";
     // s1.age = 21;
     // s1.rollno = 1234;

//     return 0;
// }