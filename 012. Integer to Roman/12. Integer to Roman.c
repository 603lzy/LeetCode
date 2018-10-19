char* intToRoman(int num) {
    char* rom[4][10] = {{"", "M", "MM", "MMM"}, {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}, {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}, {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}}; //0 - 9
    int len[10] = {0, 1, 2, 3, 2, 1, 2, 3, 4, 2};
    char* s = (char *) malloc (100);
    memset(s, 0, 100);
    int d[4] = {num % 10, num % 100 / 10, num % 1000 / 100, num / 1000}, i = 0, j, k;
    for (k = 3; k >= 0; k--)  // k is index for rom
        for (j = 0; j < len[d[k]]; j++, i++)  // j is index for each letter
            *(s + i) = *(rom[3 - k][d[k]] + j);
    return s;
}
