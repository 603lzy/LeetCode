int chrInSubStr(char* substr, int subLen, char c){
    int i = 0;
    while (i < subLen){
        if (substr[i++] == c)
            return 1;
    }
    return 0;   
}

int lengthOfLongestSubstring(char* s) {
    int sLen = strlen(s);
    if (sLen <= 1)
        return sLen;
    int subStrLen = 0, p1 = 0, p2 = 1;
    while (p2 < sLen && subStrLen < 95){
        for (p2 = p1; p2 < sLen; p2++){
            if (chrInSubStr(s + p1, p2 - p1, s[p2]) == 1)
                break;
        }
        subStrLen = (p2 - p1 > subStrLen ? p2 - p1 : subStrLen);
        p1++;
    }
    return subStrLen;
}
