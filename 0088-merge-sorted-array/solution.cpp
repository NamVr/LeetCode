class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // backwards approach
        int i = m - 1; // Pointer to last element in nums1's initial portion
        int j = n - 1; // Pointer to last element in nums2
        int k = m + n - 1; // Pointer to the last position in nums1 where we'll place elements
        
        // Work backwards from the end of nums1 and nums2
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
        
        // If there are remaining elements in nums2, copy them over
        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }
    }
};

