#ifndef STRVEC_H
#define STRVEC_H
#include<memory>
#include <string>
#include<initializer_list>

using namespace std;

class strVec{
private:
    // shared_ptr<string> elements = make_shared<string>();
    // shared_ptr<string> first_free = make_shared<string>();
    // shared_ptr<string> cap = make_shared<string>();
    static allocator<string> alloc;
    std::string *elements;
    std::string *first_free;
    std::string *cap;
    void free();
    void reallocate(size_t);
    pair<string*, string*> alloc_n_copy(const string* a, const string* b);
    void chk_n_alloc();
    
public:
    //constructor
    strVec():elements(nullptr),first_free(nullptr),cap(nullptr){}; //default
    strVec(const strVec& strvec);
    strVec(initializer_list<string> list){
        auto newdata = alloc_n_copy(list.begin(), list.end());
        elements = newdata.first;
        first_free = cap = newdata.second;
    };
    strVec& operator=(const strVec& strvec);
    //destructor
    ~strVec();

    void push_back(const string& s);

    // void push_back(const string& s){
    //     chk_n_alloc();
    //     alloc.construct(first_free++, s);
    //     return ;
    // };

    string* begin() const {return elements;}
    string* end() const {return first_free;}

    size_t size() const {return first_free - elements;}
    size_t capacity() const {return cap-elements;}
    inline void reverse(size_t);
    inline void resize(size_t, const string&);
    
};

// inline strVec::strVec(const strVec& strvec){ // copy constructor
//         pair<string*, string*> p = alloc_n_copy(strvec.elements, strvec.cap);
//         this->elements = p.first;
//         this->first_free = p.second;
//         this->cap = p.second;
//     };

// inline strVec::~strVec() { free();}

// inline void strVec::push_back(const string& s){
//     chk_n_alloc();
//     alloc.construct(first_free++, s);
//     return ;
// };

// inline void strVec::free(){
//     if (elements){
//         for (auto ptr = first_free; ptr != elements; ){
//             alloc.destroy(--ptr);
//         }
//         alloc.deallocate(elements, cap-elements);
//     }
// }

// inline void strVec::reallocate(){
//     auto newcapacity = size()? 2*size():1;
//     auto newdata = alloc.allocate(newcapacity);
//     auto dest = newdata;
//     auto elem = elements;
//     for (auto i =0; i < size();++i){
//         alloc.construct(dest++, std::move(*elem++));
//     }
//     free();
//     elements = newdata;
//     cap = elements + newcapacity;
//     first_free = dest;
//     return ;
// }

// inline strVec& strVec::operator=(const strVec& strvec){
//         auto data = alloc_n_copy(strvec.begin(), strvec.end());
//         free();
//         elements = data.first;
//         first_free = cap = data.second;
//         return *this;
//     };


// inline pair<string*, string*> strVec::alloc_n_copy(const string* a, const string* b){
//         auto data = alloc.allocate(b-a);
//         return {data, uninitialized_copy(a,b,data)};
//     }

// inline void strVec::chk_n_alloc(){
//         if (size() == capacity()) 
//             reallocate();
//     }

#endif