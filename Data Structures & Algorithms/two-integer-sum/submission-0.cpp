#include <unordered_map>
class Solution {
public:
   
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> myHashSet;   // key = first, value = second
        vector<int> sol(2);
        int diff;
        
        for(int i =0; i<size(nums); i++){
            diff = target - nums[i];
            auto test = myHashSet.find(diff);
            if(test!=myHashSet.end()){
                sol[0] = test->second;
                sol[1] =i;
                return sol;
            }
            myHashSet.insert({nums[i], i});
        }
        return sol;

    }
};
