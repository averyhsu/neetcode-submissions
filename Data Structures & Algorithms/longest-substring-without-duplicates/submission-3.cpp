class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size()==0) return 0;
        if(s.size()==1) return 1;
        unordered_map<int, int> str;
        int left = 0;
        int right = 1;
        int res = right-left;
        str.insert({s[left],0});
        while(right<s.size()){
            char val_l = s[left];
            char val_r = s[right];
            if(str.count(val_r)&&(str[val_r]+1>left)){//exist already
                left = str[val_r]+1;
                // return 100+left;
            }
            str[val_r] = right;
            right++;
            res = max(res, right-left);
        }
        return res;

    }
};
