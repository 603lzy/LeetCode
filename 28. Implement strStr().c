int strStr(char* haystack, char* needle) {
    return strstr(haystack, needle) ==  NULL ? -1 : strstr(haystack, needle) - haystack; //strstr() return the address of the first appearance
}
