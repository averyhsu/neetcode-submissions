class Solution {
public:
    int findMin(vector<int> &nums) {

        //Left and right ptr at the two ends then find mid
        //if mid > both -> left = mid because min must be to the right of middle
        // if mid >left but smaller than right then right = mid, because min must be on the left
        //impossible if mid >right  but smaller thant left then left = mid 
        // if mid<both right = mid

        //if left or right = mid, return min(left ,right)
        int left = 0; 
        int right = nums.size()-1;
        int mid = (left+right)/2;
        while(left!=mid&&right!=mid){
            int mid_val = nums[mid];
            int left_val = nums[left];
            int right_val = nums[right];
            if(mid_val>left_val&&mid_val>right_val){
                left = mid;
            }
            else if(mid_val>left_val&&mid_val<right_val){
                right = mid;
            }
            else if(mid_val<left_val&&mid_val<right_val){
                right = mid;
            }
            mid = (left+right)/2;
        }
        return min(nums[left], nums[right]);
    }
};
