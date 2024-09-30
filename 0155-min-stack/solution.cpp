class MinStack {
private:
    int tp;
    vector<int> arr;
    vector<int> minStack;

public:
    MinStack() : tp(-1) {}
    
    void push(int val) {
        arr.push_back(val); // auto assign buffer
        if (minStack.empty()) {
            minStack.push_back(val);
        } else {
            minStack.push_back(min(minStack.back(), val)); 
        }

        tp++;
    }
    
    void pop() {
        if (tp == -1) return;
        arr.pop_back(); // remove top element
        minStack.pop_back(); // remove last min element
        tp--;
    }
    
    int top() {
        return arr[tp];
    }
    
    int getMin() {
        return minStack.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
