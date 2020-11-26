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
    friend class Folder;
public:

    // default constructor
    Message(const string& s){
        MsgInfo = s;
        cout<<"MSG:"<<MsgInfo<<endl;
    }
    // copy constructor
    Message(const Message& Msg):MsgInfo(Msg.MsgInfo),FolderPtrs(Msg.FolderPtrs){
        // two different msg obj has diff ptrs
        for (auto Fptr:Msg.FolderPtrs){
            Fptr->addMsg(this); // put this mgs into folder.
        }
    }

    // copy overload
    Message& operator=(const Message& Msg){
        for (auto f:this->FolderPtrs){
            f->rmMsg(this);
        }
        this->FolderPtrs = Msg.FolderPtrs;
        for (auto ff:Msg.FolderPtrs){
            ff->addMsg(this);
        }
        this->MsgInfo = Msg.MsgInfo;
        return *this;
    }

    // move constructor

    // move overload

    // deconstructor
    ~Message();

    void save(Folder&); // put one message into folder indicated.
    
    void remove(Folder&); // delete one message from folder indicated.

    void swap(Message& lhs, Message& rhs){
        using std::swap;
        for (auto f:lhs.FolderPtrs){
            f->rmMsg(&lhs);
        }
        for (auto f:rhs.FolderPtrs){
            f->rmMsg(&rhs);
        }

        swap(lhs.MsgInfo, rhs.MsgInfo);

        swap(lhs.FolderPtrs, rhs.FolderPtrs);

        for (auto f:rhs.FolderPtrs){
            f->addMsg(&rhs);
        }
        for (auto f:lhs.FolderPtrs){
            f->addMsg(&lhs);
        }
    }
    
    
private:
    std::set<Folder*> FolderPtrs; // what folders this message saved 
    string MsgInfo;
};

inline
void Message::save (Folder& folder){
    // put this message in folder.
    folder.addMsg(this);
    FolderPtrs.emplace(&folder);
    return ;
}

inline
void Message::remove(Folder& folder){
    folder.rmMsg(this); // remove this msg from folder.
    FolderPtrs.erase(&folder);
}

inline
Message::~Message(){
    for (auto Fptr:this->FolderPtrs){
        Fptr->rmMsg(this);
    }
};
#endif