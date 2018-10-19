int cmpstr(char *str, int cmp_len) {
		int i = 0, j = 0; // j = i % cmp_len
		while (*(str + i) != '\0') {
			j = 0;
			while (j < cmp_len)
				if (*(str + i++) != *(str + j++))
					return 0;	
		}
		return (cmp_len == j);
}
bool repeatedSubstringPattern(char* str) {// str point to the start of the string
    int lencmp = 1;
	int max_len_sub = strlen(str) / 2; // max length of a substring
	while (lencmp <= max_len_sub)  
		if(cmpstr(str, lencmp++))
			return 1;
	return 0;
}
