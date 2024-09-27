class MyCalendarTwo {
private:
    unordered_map<int,int> non_overlapping;
    unordered_map<int,int> overlapping;
public:
    MyCalendarTwo() {
        // none
    }
    
    bool book(int start, int end) {
        for (const auto& [s,e] : overlapping) {
            // list for double booking.
            if (end > s && e > start) return false;
        }

        for (const auto& [s,e] : non_overlapping) {
            // list for single booking
            if (end > s && e > start) {
                overlapping.insert({max(start,s), min(end,e)});
            }
        }
        non_overlapping.insert({start,end});

        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */
