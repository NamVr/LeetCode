class Solution {
public:
    string intToRoman(int num) {
        string o[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        string te[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        string h[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        string t[] = {"", "M", "MM", "MMM"};

        return t[num/1000] + h[(num%1000)/100] + te[(num%100)/10] + o[num%10];
    }
};