class RandomizedSet {
public:
    unordered_map<int,int> mp;
    vector<int> l;

    RandomizedSet() {}
    
    bool insert(int val) {
        bool res = mp.find(val) == mp.end();
        if (res) {
            mp[val] = l.size();
            l.push_back(val);
        }
        return res;
    }
    
    bool remove(int val) {
        bool res = mp.find(val) != mp.end();
        if (res) {
            int idx = mp[val];
            int lastVal = l.back();
            l[idx] = lastVal;
            l.pop_back();
            mp[lastVal] = idx;
            mp.erase(val);
        }
        return res;
    }
    
    int getRandom() {
        return l[rand() % l.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
