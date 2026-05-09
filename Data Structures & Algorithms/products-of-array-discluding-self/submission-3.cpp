class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> left_pass (nums.size());
        vector<int> right_pass(nums.size());
        vector<int> res (nums.size());
        for(int i =0; i< nums.size(); i++){
            if(i == 0){
                left_pass[i] = 1;
            }
            else if(i == 1){
                left_pass[i] = nums[0];
            }
            // i >1;
            else {
                left_pass[i] = nums[i-1] *left_pass[i-1];
            }
        }        
        for (int i = nums.size()-1; i>=0; i--){
            if(i == nums.size()-1){
                right_pass[i] = 1;
            }
            else if(i == nums.size()-2){
                right_pass[i] = nums[nums.size()-1];
            }
            else{
                right_pass[i] = nums[i+1]*right_pass[i+1];
            }
        }
        for(int i =0 ;i<nums.size(); i++){
            res[i] = right_pass[i]*left_pass[i];
        }
        return res;

    }
};
