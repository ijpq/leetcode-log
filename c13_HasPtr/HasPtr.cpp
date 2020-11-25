//行为像值的类
#include "HasPtr.h"
#include <string>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

inline 
void swap(HasPtr& p1, HasPtr& p2){
    using std::swap;
    cout<<"swap hasptr :"<<*p1.ps<<" and hasptr: "<<*p2.ps<<endl;
    swap(p1.ps, p2.ps);
    swap(p1.i, p2.i);
}

int main(){
    string s1 = "abd";
    string s2 = "abc";
    HasPtr p1(s1);    
    HasPtr p2(s2);
    p1 = p2;

    // swap, operator<
    // vector<HasPtr> vec{HasPtr{string("a"), 1}, HasPtr{string("b"),2}, HasPtr{string("c"),3}};
    vector<HasPtr> vec;
    HasPtr p1 = HasPtr(string("a"), 3);
    HasPtr p2(string("b"), 2);
    HasPtr p3(string("c"), 4);
    // vec.push_back(HasPtr{string("a"), 3});
    // vec.push_back(HasPtr{string("b"), 2});
    // vec.push_back(HasPtr{string("c"), 4});
    vec.push_back(p1);
    vec.push_back(p2);
    vec.push_back(p3);
    sort(vec.begin(), vec.end());
    
    return 0;

}