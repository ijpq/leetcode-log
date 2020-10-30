// // // #include <iostream>
// // // #include <vector>
// // // #include <queue>
// // // using namespace std;
// // // typedef struct {float a,b,c,d,e,f;} Body;
// // // int main(){
// // //     int size = sizeof(Body);
// // //     cout<<size<<endl;

// // //     return 0;
// // // }






// // #include <bits/stdc++.h>
// // #define mk make_pair
// // using namespace std;
// // map<string,int> dish;
// // map<pair<string,string>,int> order;
 
// // int main()
// // {
// //     int n,m;
// //     cin>>n>>m;
// //     for(int i = 0 ; i < n ; i ++)
// //     {
// //         string s;int x;
// //         cin>>s>>x;
// //         dish[s] = x;
// //     }
// //     for(int i = 0 ; i < m ; i ++)
// //     {
// //         string opt,name,cai;
// //         cin>>name>>opt>>cai;
// //         if(opt == "order")
// //         {
// //             if(dish[cai] && order[mk(name,cai)] == 0)
// //             {
// //                 cout<<"yes"<<endl;
// //                 dish[cai] --;
// //                 order[mk(name,cai)] = 1;
// //             }
// //             else
// //                 cout<<"no"<<endl;
// //         }
// //         else
// //         {
// //             if(order[mk(name,cai)])
// //             {
// //                 cout<<"yes"<<endl;
// //                 order[mk(name,cai)] = 0;
// //                 dish[cai] ++;
// //             }
// //             else
// //                 cout<<"no"<<endl;
// //         }
// //     }
// // }


// // #include <bits/stdc++.h>
// // #define mk make_pair
// // using namespace std;
// // const int N = 2e7 + 15;
// // int dp[20][N / 20];
// // int prime[N], mark[N], pcnt;
// // int a[20];
// // int n, m;

// // void getPrimes()
// // {
// //     memset(mark, 0, sizeof(mark));
// //     mark[0] = mark[1] = 1;
// //     pcnt = 0;
// //     for (int i = 2; i < N; i++)
// //     {
// //         if (!mark[i])
// //             prime[pcnt++] = i;
// //         for (int j = 0; i * prime[j] < N && j < pcnt; j++)
// //         {
// //             mark[i * prime[j]] = 1;
// //             if (i % prime[j] == 0)
// //                 break;
// //         }
// //     }
// // }

// // int dfs(int pos, int sum, int sel)
// // {
// //     //cout<<pos<<" "<<sum<<" "<<sel<<endl;
// //     if (mark[sum] == 0 && sel == m)
// //         return 1;
// //     if (dp[pos][sum] != -1)
// //         return dp[pos][sum];
// //     if (pos >= n || sel > m || n - pos + sel < m)
// //         return 0;
// //     dp[pos][sum] = dfs(pos + 1, a[pos] + sum, sel + 1) + dfs(pos + 1, sum, sel);
// //     return dp[pos][sum];
// // }

// // int main()
// // {
// //     getPrimes();
// //     memset(dp, -1, sizeof(dp));
// //     cin >> n >> m;
// //     for (int i = 0; i < n; i++)
// //         cin >> a[i];
// //     cout << dfs(0, 0, 0) << endl;
// // }

// #include 
// #include 
// #define sd(a) scanf("%d",&a)
// using namespace std;
// const int N=20+5;
// int n,K,val[N];
// int isprime(int x)
// {
// int flag=0;
// for(int i=2;i {
// if(!(x%i))
// {
// flag=1;
// break;
// }
// }
// return flag^1;
// }
// int dfs(int pos,int k,int ans) //选到第pos个位置,已经选了k个数的和为ans；
// {
// if(pos==n+1||k==K) //把数组遍历完或者已经选了k个数
// {
// if(k==K&&isprime(ans)) //k==K,且选好的数的和是prime。
// return 1;
// return 0;
// }
// return dfs(pos+1,k+1,ans+val[pos])+dfs(pos+1,k,ans);
// }
// int main()
// {
// scanf("%d%d",&n,&K);
// for(int i=1;i printf("%d\n",dfs(1,0,0)); //从第一个位置开始,已选0个数和为0.
// }




// #include <bits/stdc++.h>
// using namespace std;

// struct node{
//     int cos;
//     int wei;
//     int val;
//     node (){}
//     friend bool operator < (const node &a1, const node &a2){
//         if (a1.val == a2.val){
//             if (a1.cos == a2.cos){
//                 return a1.wei < a2.wei;

//             }
//             return a1.cos < a2.cos;
//         }
//         return a1.val > a2.val;
//     }
// }a[100005];

// int n,m,kk;
// int dp[101][10005];

// int main(){
//     scanf("%d%d%d", &n, &m, &kk);
//     for (int i = 0; i < n; i++){
//         scanf("%d%d%d", &a[i].cos, &a[i].wei, &a[i].val);
//     }

//     sort(a,a+n);
//     for (int i = 0; i < n; i ++){
//         if (a[i].val < a[0].val){
//             n=i;
//             break;
//         }
//     }

//     for (int i = 0; i < n; i++){
//         for (int k = m; k>=a[i].wei; k--){
//             for (int j = kk; j>=a[i].cos; j--){
//                 dp[k][j] = max(dp[k][j], dp[k-a[i].wei][j-a[i].cos]+1);
//             }
//         }
//     }
//     cout<<dp[m][kk]<<endl;
//     return 0;
// }


// // #include <bits/stdc++.h>
// #include <iostream>
// #include <unordered_map>

// // #define DEBUG(...) printf(__VA_ARGS__);

// // template<typename in, typename out>
// // out f(in a){
// //     return a;
// // }

// class Node{
//     public:
//         Node();
//         Node(int v);
//         Node(int v) {
//             int val = v;
//             class Node left;
//             class Node right;
//         }
// };

// using namespace std;
// int main(){
//     unordered_map<string, Node> map;
//     // int a = 0;
//     // DEBUG("aaaaa")
//     // // int* d = &a, x = &a;
//     // auto c = f(a);
//     // cout<<c<<endl;
//     // int& b = a;
//     // int &c = a;
//     // cout<<"gcc3"<<endl;

    
//     return 0;
// }

#include <iostream>
#include <string>
#include <vector>
using namespace std;


class Solution {
public:
    void kmp(string& pattern, vector<int>& prefix){
        // static vector<int> prefix={0};
        int nLength = pattern.size();
        for (int i =1; i<pattern.size(); ++i){
            int j = 0, val =0, iptr=i;

            while (j < iptr){
                if (pattern[j] == pattern[iptr]){
                    j += 1;
                    iptr -= 1;
                    val += 1;
                }
                else break;
            }
            prefix.push_back(val);
        }
        return;
    }
    int strStr(string haystack, string needle) {
        int length = needle.size();
        vector<int> prefix = {0};
        kmp(needle, prefix);
        int nptr = 0,ptr=0;
        for (ptr = 0; ptr < haystack.size(); ptr++){
            if (nptr == needle.size()){ // if haystack lager than needle
                return ptr-nptr;
            }
            if (needle[nptr] != haystack[ptr]){ // find prefix
                nptr = prefix[nptr-1];
                ptr--;
            }
            else{
                nptr++;
            }
        }
        if (nptr < length) return -1; // false
        if (nptr == length) {
            return ptr-nptr; // same length
        }
        return 0;


    }
};


int main(){
    Solution sol;
    sol.strStr("aaab","aab");
    return 0;
}