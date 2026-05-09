class Solution {
public:
    int maxProfit(vector<int>& prices) {
        //I have two pointers, starts at idx 0 and 1, 
        //I compare val[1] to val[0], if val[1] is bigger or equal, I see if
        //the profit gives max profit (and save)
        //else if val[1] is smaller, I can discard val[0] as I know it will not 
        //be the best buy point and move my new left pter to val[1]
        int res = 0;
        int left = 0;
        int right = 1;
        while(right<prices.size()){
            if(prices[right]>=prices[left]){
                int prof = prices[right]-prices[left];
                res = max(res, prof);
            }
            else //pr<pl
            {
                left = right;
            }
            right++;

        }
        return res;
    }
};
