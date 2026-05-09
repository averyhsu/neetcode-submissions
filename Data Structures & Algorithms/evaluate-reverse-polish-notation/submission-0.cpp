class Solution {
private:
    stack<int> stk;
    void action(string op){
        int one = stk.top();
        stk.pop();
        int two = stk.top();
        stk.pop();
        if(op=="+") stk.push(two+one);
        if(op=="-") stk.push(two-one);
        if(op=="*") stk.push(two*one);
        if(op=="/") stk.push(two/one);



    }
public:
    int evalRPN(vector<string>& tokens) {
        for(int i = 0; i<tokens.size();i++){
            string val = tokens[i];            
            if(val=="+"){
                action(val);
            }
            else if(val=="-") action(val);
            else if(val == "*") action(val);
            else if(val == "/") action(val);
            else stk.push(stoi(val));
        }
        return stk.top();
    }
};

