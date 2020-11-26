#ifndef FOLDER_H
#define FOLDER_H
#include"Message.h"
#include<set>
class Message;
class Folder{
    // friend class Message;

public:
    Folder() = default;
    Folder(const Folder& Fref):MessagePtr(Fref.MessagePtr){
        for (auto Mptr:Fref.MessagePtr){
            Mptr->FolderPtrs.insert(this);
        }
        
    }

    Folder& operator=(const Folder& Fref){ // non const!!!
        if (this != &Fref){
            for (auto Mptr: MessagePtr){
                Mptr->FolderPtrs.erase(this);
            }
            this->MessagePtr = Fref.MessagePtr;
            for (auto Mptr:Fref.MessagePtr){
                Mptr->FolderPtrs.insert(this);
            }
        }
        return *this;
    }

    // ~Folder();
    void rmMsg(Message*);
    
    void addMsg(Message*);
private:
    std::set<Message*> MessagePtr;
};
inline
void Folder::rmMsg(Message* MsgPtr){
    MessagePtr.erase(MsgPtr);

}

inline
void Folder::addMsg(Message* MsgPtr){
    MessagePtr.emplace(MsgPtr);
}

inline
Folder::~Folder(){
    for (auto Mptr:this->MessagePtr){
        Mptr->FolderPtrs.erase(this);
    }
    // this->MessagePtr.clear();
}

#endif