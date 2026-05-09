#include <unordered_map>
#include <algorithm>  //
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
        
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hash;
        string sorted;
        for(int i =0; i<size(strs);i++){
            sorted = strs[i];
            std::sort(sorted.begin(), sorted.end());
            hash[sorted].push_back(strs[i]);
        }

        vector<vector<string>> res;
        for (auto& [key, value] : hash) {
            res.push_back(value);
        }
        return res;
    }

};
