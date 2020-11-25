#ifndef STRING_H
#define STRING_H

#include<memory>

using namespace std;
class String{
private:
    size_t sz;
    static allocator<char> alloc;
    char* elements;
    char* first_free;
    char* cap;
    
    
public:
    String():elements(nullptr), first_free(nullptr), cap(nullptr){};
    String(const char* s):sz(std::strlen(s)),elements(alloc.allocate(sz)){
        std::uninitialized_copy(s, s+sz, elements);
    }
};
#endif
