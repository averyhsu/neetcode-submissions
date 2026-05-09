
#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<int, int> hash;
        char cur;
        for (int i =0; i<size(s); i++)
        {
            cur = s[i];
            hash[cur]++;
        }
        for(int i =0; i<size(t);i++){
            cur = t[i];
            hash[cur]--;
            if(hash[cur]==0){
                hash.erase(cur);

            }
        }
        return hash.empty();
    }
};
