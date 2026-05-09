#include <unordered_set>

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        //let key be nums, value be longest consec seq
        

        std::unordered_set<int> set; //seq-> seq length
        

        int answ = 0;
        for(int i = 0; i<nums.size();i++){
            int val = nums[i];
            set.insert(val);
        }

        for(int i = 0; i<nums.size();i++){
            int val = nums[i];
            if(set.find(val-1)!=set.end()){
                continue;
            }
            // It is the begining of a sequence
            int length=1;
            while(set.find(val+length)!=set.end()){
                length++;
            }
            if (length>answ){
                answ = length;
            }
        }
        return answ;
    }
};
