#ifndef MSG_H
#define MSG_H
#include<string>
#include<vector>
#include<memory>
#include<iostream>
#include<utility>
#include<set>
#include"Folder.h"

using namespace std;
class Folder;
class Message{
public:
    // default constructor
    Message(const string& s){
        msg_info = s;
        cout<<msg_info<<endl;
    }
    // copy constructor

    // copy overload

    // move constructor

    // move overload

    // deconstructor

    void save(Folder&);
    
    void remove(Folder&);
    
    
private:
    set<Folder*> FolderPtrs;
    string msg_info;
};


#endif