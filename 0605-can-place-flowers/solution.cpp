class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int size = flowerbed.size();

        for (int i = 0; i < size; i++) {
            if (!flowerbed[i]) {
                // it is zero.

                if ((!i || !flowerbed[i-1]) && (i == size-1 || !flowerbed[i+1])) {
                    flowerbed[i] = 1;
                    n--;
                    if (n == 0) return true;
                }
            }
        }

        return n <= 0;
    }
};
