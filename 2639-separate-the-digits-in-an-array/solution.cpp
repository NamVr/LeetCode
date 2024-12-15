class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> ans;

        for (int &a : nums) {
            // for each element in nums convert it to string
            string b = to_string(a);

            for (char &c : b) {
                // for each char in string b
                ans.push_back(c-'0');

                /**
                In C++, "c - '0'" means subtracting the ASCII value of the character '0' from the character 'c',
                effectively converting the character 'a' into its corresponding integer value
                TLDR: convert character to integer using ASCII conversion
                **/
            }
        }

        return ans;
    }
};
