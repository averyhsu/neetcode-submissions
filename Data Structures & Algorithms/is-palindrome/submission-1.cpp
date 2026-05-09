class Solution {
public:
    bool isPalindrome(string s) {
        std::string h;  
        for(int i = 0; i<s.length(); i++){
            if(s[i]==32||s[i]<48 || (s[i]>57 && s[i]<65)||(s[i]>90 && s[i]<97)||s[i]>122) {
                continue;
            }
            if(s[i]>90){
                s[i] = s[i]-32;
            }
            h+=(s[i]);
        }


        size_t last_index = h.length()-1;
        size_t len = last_index+1;
        int stop = len/2;
        for(int i =0; i<stop;i++){
            if(h[i]!=h[last_index-i]) return false;
        }
        return true;
    }
};
