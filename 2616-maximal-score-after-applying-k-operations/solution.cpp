class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<int> maxHeap; // max heap

        for (int num: nums) {
            maxHeap.push(num); // O(n) space
        }

        long long score = 0;

        for (int i = 0; i < k; i++) {
            int largest = maxHeap.top(); // get largest element
            maxHeap.pop();

            score += largest;
            maxHeap.push((largest + 2) / 3);
        }

        return score;
    }
};
