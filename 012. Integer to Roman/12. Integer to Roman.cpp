class Solution {
public: // Use dict to convert 0 - 3999 to Roman
    string intToRoman(int num) {
        char* rom3[4] = {"", "M", "MM", "MMM"};                                        //0XXX - 3XXX
        char* rom2[10] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}; //0XX - 9XX
        char* rom1[10] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}; //0X - 9X
        char* rom0[10] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}; //0 - 9
        string s;
        s += rom3[num / 1000];  //X...
        s += rom2[num % 1000 / 100];  //.X..
        s += rom1[num % 100 / 10];  //..X.
        s += rom0[num % 10];  //...X
        return s;
    }
};
