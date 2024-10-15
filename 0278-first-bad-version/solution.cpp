// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        if (n == 1) return 1;
        int l = 0;

        while (l <= n) {
            int m = l + (n-l)/2;

            // if middle is a bad version, then all versions after middle are bad.
            if (isBadVersion(m)) {
                // base condition, if just the previous version is good, then return this.
                if (!isBadVersion(m-1)) return m;
                n = m-1;
            } else l = m+1;
            // if middle is good version, then previous versions are good, search the next.
        }

        return 0;
    }
};
