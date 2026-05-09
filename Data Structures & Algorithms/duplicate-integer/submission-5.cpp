#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> hashSet; // For storing integers
        for(int i =0; i<size(nums);i++){

             if((hashSet.insert(nums[i]).second)==0){
                return true;
             }
        }
        return false;
    }
};