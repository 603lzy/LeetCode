class Solution {
public:
    string intToRoman(int num) {
        char* rom3[4] = {"", "M", "MM", "MMM"};
        char* rom2[10] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}; //0XX - 9XX
        char* rom1[10] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}; //0X - 9X
        char* rom0[10] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}; //0 - 9
        int d[4];
        d[0] = num % 10;
        d[1] = num % 100 / 10;
        d[2] = num % 1000 / 100;
        d[3] = num / 1000;
        string s;
        s += rom3[d[3]];
        s += rom2[d[2]];
        s += rom1[d[1]];
        s += rom0[d[0]];
        return s;
    }
};
