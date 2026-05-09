class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        //loop through  
            //Store temp + idx as a pair in a stack
            //if temp smaller than top stack, add it to stack
            //if temp bigger than top stack, pop top stack and compute idx diffference
                //this is where we get the #of days
                //we can store this in corresponding return vector idx
            
        stack<std::pair<int, int>> stk;
        vector<int> res (temperatures.size(), 0);
        for(int i = 0; i<temperatures.size();i++){
            int temp = temperatures[i];
            if(stk.empty()) {
                stk.push({temp, i});
                
            }
            else if (temp<stk.top().first){
                stk.push({temp, i});
                
            }
            else{///temp>stk.top()
                while((!stk.empty())&&temp>stk.top().first){
                    int idx = stk.top().second;
                    int days = i-idx;
                    res[idx] = days;
                    stk.pop();
                }
                stk.push({temp, i});
            }
        }
        return res;
    }
};
