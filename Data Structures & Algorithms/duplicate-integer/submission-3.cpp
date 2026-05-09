class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        vector<int> pos_count(size(nums));
        vector<int> neg_count(size(nums));

        
        for(int i = 0; i<size(nums); i++){
            
               
            if(nums[i]>=0){
                if(nums[i]>= size(pos_count)){
                    pos_count.resize(nums[i]*2);
                }
                pos_count[nums[i]]++;
                if (pos_count[nums[i]] >=2 ){
                    return true;
                }
            }
            else{
                int num = nums[i]*(-1);
                if(num >= size(neg_count)){
                    neg_count.resize(num*2);
                }
                neg_count[num]++;
                if (neg_count[num] >=2 ){
                    return true;
                }
            }
            
        }
        return false;
    }
};