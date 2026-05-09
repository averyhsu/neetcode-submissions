#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        const int n = nums.size();

        for (int i = 0; i < n; ++i) {
            // skip duplicate first elements
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            // optional early break: if current > 0, sums will be > 0
            if (nums[i] > 0) break;

            int target = -nums[i];
            int l = i + 1, r = n - 1;

            while (l < r) {
                long long sum = (long long)nums[l] + nums[r];
                if (sum == target) {
                    res.push_back({nums[i], nums[l], nums[r]});
                    // skip duplicates for l and r
                    int lv = nums[l], rv = nums[r];
                    while (l < r && nums[l] == lv) ++l;
                    while (l < r && nums[r] == rv) --r;
                } else if (sum < target) {
                    ++l;
                } else {
                    --r;
                }
            }
        }
        return res;
    }
};
