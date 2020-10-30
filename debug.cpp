//
// Created by ke tang on 2020/4/26.
//

//#include "debug.h"
//#include <iostream>
//#include <vector>
//#include <numeric>
//#include <string>
//using namespace std;
//int declarition(){
//    cout<<"func declarition"<<endl;
//    vector<int> ivec(10);
//    string s ="sss";
//    auto cnt = ivec.size();
//    iota(ivec.begin(), ivec.end(), 0);
//    for (auto r: ivec){
//        cout<<r<<endl;
//    }
//    for (auto r = ivec.begin(); r!=ivec.end(); ++r){
//        *r *= 2;
//
//    }
//    for (auto r: ivec){
//        cout<<r<<endl;
//    }
//
//    return 0;
//}
//string::size_type func1(const string &, char, string::size_type &);
//string::size_type func1(const string &s, char c, string::size_type &occurs){
//    auto ret = s.size();
//    occurs = 0;
//    for (decltype(ret) i = 0; i!= s.size(); ++i){
//        if (s[i] == c){
//            if (ret==s.size()) ret=i;
//            ++occurs;
//        }
//    }
//    return ret;
//
//
//}
//
//vector<string> func2();
//vector<string> func2(){
//    return {"a","b"};
//}
//



////    const int &i = 10;
////    cout<<i<<endl;
////    cout<<"hi"<<endl;
//////    declarition();
////    string s("asfafgag");
////    decltype(s.size()) occurs = 0;
//////    func1(s, 's', occurs);
////
////    vector<string> s2 = func2();
//    Solution obj;
//    vector<int> s(3);
//    iota(s.begin(),s.end(),1);
//    obj.nextPermutation(s);

//


//sougou1
// class Solution
// {
// public:
//     int numberofprize(int a, int b, int c)
//     {
//         int maxx = a, minn = a;
//         if (b > maxx)
//             maxx = b;
//         if (c > maxx)
//             maxx = c;
//         if (b < minn)
//             minn = b;
//         if (c < minn)
//             minn = c;
//         int l = minn, r = maxx;
//         int ans = minn;
//         while (l <= r)
//         {
//             int mid = (l + r) / 2;
//             int need = 0, rem = 0;
//             if (a > mid)
//                 rem += a - mid;
//             else
//                 need += mid - a;
//             if (b > mid)
//                 rem += b - mid;
//             else
//                 need += mid - b;
//             if (c > mid)
//                 rem += c - mid;
//             else
//                 need += mid - c;
//             if (rem >= need * 2)
//             {
//                 ans = max(ans, mid);
//                 l = mid + 1;
//             }
//             else
//                 r = mid - 1;
//         }
//         return ans;
//     }
// };


//sogou2
class Solution
{
public:
    int solve(int t, int *xa, int n)
    {
        int res = 0;
        for (int i = 0; i < n; i += 2)
        {
            if (i == 0)
                res++;
            else
            {
                if (xa[i] * 2 - xa[i + 1] - t * 2 >= xa[i - 2] * 2 + xa[i - 1])
                {
                    res++;
                }
            }
            if (i == n - 3)
                res++;
            else
            {
                if (xa[i] * 2 + xa[i + 1] + t * 2 < xa[i + 2] * 2 - xa[i + 3])
                {
                    res++;
                }
            }
        }
        return res;
    }
};