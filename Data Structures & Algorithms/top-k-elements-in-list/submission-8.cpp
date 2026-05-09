#include <unordered_map>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        int max_count=0;
        unordered_map<int, int> count;
        for(int val:nums){
            count[val]++;  
            if (count[val]>max_count){
                max_count=count[val] ;
            }       
        }

        vector<vector<int>> bucket (max_count+1);
        for (auto& p : count) {
            bucket[p.second].push_back(p.first);
        }

        int iter = 0;
        int cond = 0;
        while (cond!= k){
            if(bucket[max_count-iter].size()!=0){
                res.insert(res.end(), bucket[max_count-iter].begin(), bucket[max_count-iter].end());
                cond=cond+bucket[max_count-iter].size();
            }

            iter++;
        }
        return res;
    }
};
