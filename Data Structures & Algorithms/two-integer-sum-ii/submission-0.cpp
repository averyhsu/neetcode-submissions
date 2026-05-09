class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 0;
        int end = numbers.size()-1;
        vector<int> res(2);
        int sum = numbers[start]+numbers[end];
        while((sum!=target)){
            if(sum>target){
                end = end-1;
            }
            else{
                start = start+1;
            }
            sum = numbers[start]+numbers[end];
        }
        res[0] = start+1;
        res[1]  = end+1;
        return res;
        
    }
};
