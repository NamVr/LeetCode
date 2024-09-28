#include <vector>

class MyCircularDeque {
private:
    int size, k, front, rear;
    vector<int> q;

public:
    MyCircularDeque(int k): k(k), q(k), rear(k-1), front(0), size(0) {}
    
    bool insertFront(int value) {
        if (size == k) return false; // overflow
        
        front = (front - 1 + k) % k;
        q[front] = value;
        
        size++;
        return true;
    }
    
    bool insertLast(int value) {
        if (size == k) return false; // overflow

        rear = (rear + 1) % k;
        q[rear] = value;

        size++;
        return true;
    }
    
    bool deleteFront() {
        if (!size) return false; // underflow

        front = (front + 1) % k;

        size--;
        return true;
    }
    
    bool deleteLast() {
        if (!size) return false; // underflow

        rear = (rear - 1 + k) % k;

        size--;
        return true;
    }
    
    int getFront() {
        if (!size) return -1;

        return q[front];
    }
    
    int getRear() {
        if (!size) return -1;

        return q[rear];
    }
    
    bool isEmpty() {
        return !size;
    }
    
    bool isFull() {
        return size == k;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
