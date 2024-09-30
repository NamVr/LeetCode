class CustomStack {
private:
    vector<int> arr;
    int maxSize;
    int top;

public:
    CustomStack(int maxSize) : maxSize(maxSize), top(-1) {
        arr.resize(maxSize); // Allocate space for the stack
    }
    
    void push(int x) {
        if (top == maxSize-1) return;
        arr[++top] = x;
    }
    
    int pop() {
        if (top == -1) return -1;
        return arr[top--];
    }
    
    void increment(int k, int val) {
        // bottom increment.
        int limit = min(k, top + 1); 
        for (int i = 0; i < limit; i++) {
            arr[i] += val;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
