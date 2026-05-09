class MinStack {
private:
    stack<int> cur_min;
    stack<int> stk;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        if(stk.empty()){
            stk.push(val);
            cur_min.push(val);
        }
        else{
            stk.push(val);
            int min = cur_min.top();
            if(val<min) cur_min.push(val);
            else cur_min.push(min);
        }
       
    }
    
    void pop() {
        stk.pop();
        cur_min.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return cur_min.top();
    }
};
