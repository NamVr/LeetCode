class Solution {
public:
    bool areAlmostEqual(string s1, string s2) {
        int i = 0, j = 0, diff = 0;

        for (int n = 0; n < s1.size(); n++) {
            // store difference
            if (s1[n] != s2[n]) {
                diff++;

                if (diff > 2) {
                    return false; // one swap will not make any difference now
                } else if (diff == 1) {
                    // first swap, store it
                    i = n;
                } else {
                    // second swap, store it
                    j = n;
                }
            }
        }

        // after one pass iteration, check if swap is possible?
        return (s1[i] == s2[j] && s1[j] == s2[i]);
    }
};
