class Solution {
public:
 
    bool isValid(string s) {
        map<char,char> bracket = {{')', '('}, {']','['}, {'}', '{'}};
        stack<char> stack;
        //loop through string, 
        //if see left bracket add to stack, 
        //else inspect and check if left bracket is in stack
        //if yes contiue
        //else false
        for(int i = 0; i<s.size();i++){
            if(s[i]=='('||s[i]=='['||s[i]=='{'){
                stack.push(s[i]);
            }
            else{
                if(stack.empty()||stack.top()!=bracket[s[i]]) return false;
                else stack.pop();
            }
        }
        return stack.empty();
    }
};
