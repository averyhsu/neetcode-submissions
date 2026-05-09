class Solution {
public:
    int k2h (vector<int>& piles, int k){
        int res=0;
        for(int i =0; i<piles.size();i++){
            if(piles[i]<k) res++;
            else{// piles[i]>=k
                res = res+((piles[i] +k-1)/k);
            }
        }
        return res;
    }
    
    int minEatingSpeed(vector<int>& piles, int h) {
        int max = *max_element(piles.begin(), piles.end());
        int left = 1;
        int right = max;
        while(left<right){
            int mid = (right+left)/2;
            if(k2h(piles, mid)<=h){
                right = mid;
            }
            else{
                left = mid+1;
            }
        }
        return left;

    }
};
