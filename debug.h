//
// Created by ke tang on 2020/4/26.
//


#ifndef LEETCODE_LOG_DEBUG_H
#define LEETCODE_LOG_DEBUG_H
#include <vector>
#include <iostream>
using namespace std;
int declarition();
class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        auto pivot = intervals.begin();
        while (pivot != intervals.end()-1){
            auto cmpptr = pivot+1; //目前检查的pair
            auto curptr = pivot;
            while (curptr >= intervals.begin() && curptr < intervals.end()){
                if ((*cmpptr)[0] > (*curptr)[0]){
                    pivot++;
                    break;
                }
                else if ((*cmpptr)[0] == (*curptr)[0]){
                    if ((*cmpptr)[1] <= (*curptr)[1]){
                        pivot++;
                        break;
                    }
                    else{
                        curptr--;
                        continue;
                    }
                }
                else{
                    curptr--;
                    continue;
                }
            }
            intervals.insert(curptr+1, *cmpptr);
            intervals.erase(cmpptr+1);
            pivot++;
        }
        return 0;


    }
};

#endif //LEETCODE_LOG_DEBUG_H
