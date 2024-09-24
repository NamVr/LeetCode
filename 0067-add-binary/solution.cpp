class Solution {
public:
    string addBinary(string a, string b) {
        int carry = 0;
        string ans = "";
        int i = a.length() - 1, j = b.length() - 1;

        while (i >= 0 || j >= 0 || carry > 0) {
            int A = (i >= 0) ? a[i] - '0' : 0;
            int B = (j >= 0) ? b[j] - '0' : 0;

            int sum = A + B + carry;
            ans.push_back((sum % 2) + '0');
            carry = sum / 2;

            i--;
            j--;
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};
