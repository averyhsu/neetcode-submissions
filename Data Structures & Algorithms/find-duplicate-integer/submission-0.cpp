class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        //array basically creates a linked list with cycle
        //slow and fast pointer-->find intersection
        int slow =0;
        int fast = 0;
        while(slow!=fast||slow==0){
            int slow_next = nums[slow];
            slow = slow_next;
            int fast_next = nums[nums[fast]];//update two index at once
            fast = fast_next;
        }
        //Floyd's leave slow at intersection, move fast to 0
        //shift each by one and intersection is answer
        fast = 0;
        while(slow!=fast){
            int slow_next = nums[slow];
            slow  = slow_next;
            int fast_next = nums[fast];
            fast = fast_next;
        }
    
        
        return fast;
    }
};
