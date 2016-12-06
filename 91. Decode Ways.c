int numDecodings(char* s) {
	int lens = strlen(s);
	int *dw = malloc((lens + 1) * sizeof(int));
	int i;
	char p[3], str1[3] = "09", str2[3] = "26";
	p[2] = '\0';
	if (lens == 0 || s[0] == '0')
		return 0;
	if (lens == 1)
		return 1;
  //lens > 1 dp   
	*dw = 1;
	*(dw + 1) = 1;
	for (i = 2; i <= lens; i++) {
		if (s[i - 1] != '0')
			*(dw + i) = *(dw + i - 1);
		else
			*(dw + i) = 0;
		p[0] = s[i - 2];
		p[1] = s[i - 1];
		if (strcmp(str1, p) < 0 && strcmp(p, str2) <= 0)
			*(dw + i) += *(dw + i - 2);
		}	
	return *(dw + lens);
}
