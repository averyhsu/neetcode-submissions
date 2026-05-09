class Solution {
public:
    int find_max(unordered_map<int, int> count){
        int res = 0;
        for (auto &p : count) {
            char key = p.first;
            int value = p.second;
            res = max(res, value);
        }
        return res;
    }
    int characterReplacement(string s, int k) {
        int len = s.size();
        if (len==1) return 1;
        int res = 0;
        
        unordered_map<int, int> count;
        int left = 0;
        int right=1;
        char head = s[left];
        char tail = s[right];
        count[head] =1;
        if(count.count(tail)) count[tail]++;
        else count[tail]=1;

        while(right<len){
            
            int length = right-left+1;
            if(length-find_max(count)>k){
                count[s[left]]--;
                left++;
                // if(count.count(s[left])) count[s[left]]++;
                // else count[s[left]] =1;
           
                //im not entering this conndition
            }
            else{//<=k
                res = max(res, length);
                right++;
                tail = s[right];

                if(count.count(tail)) count[tail]++;
                else count[tail]=1;
            }
        }
        return res;
    }
};