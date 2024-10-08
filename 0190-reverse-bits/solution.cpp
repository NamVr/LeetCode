class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t a = 0;

        for (int i = 0; i < 32; i++) {
            int bit = (n >> i) & 1;
            a = a | (bit << (31-i));
        }

        return a;
    }
};
