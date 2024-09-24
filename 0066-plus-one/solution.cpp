class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 0;
        for (int i = digits.size()-1; i >= 0; i--) {
            int sum = digits[i] + carry + ((i == digits.size()-1) ? 1 : 0);
            if (sum >= 10)
                carry = sum / 10;
            else 
                carry = 0;
            digits[i] = sum % 10;
        }

        if (carry) digits.insert(digits.begin() + 0, carry);
        return digits;
    }
};
