class Solution {
public:
    int mySqrt(int x) {
        long r = x; // type conversion

        while (r*r > x) {
            r = (r + x/r)/2;
        }
        
        return r;
    }
};
