int compInc(const void *a, const void *b) {//to increase sort
	return *(int*)a - *(int*)b;
}

int findContentChildren(int* g, int gSize, int* s, int sSize) {
	int cnt = 0, i, j = 0, k = 0;
	qsort(g, gSize, sizeof(g[0]), compInc);
	qsort(s, sSize, sizeof(s[0]), compInc);
	for (i = 0; i < gSize && g[i] <= s[sSize - 1]; i++) {
		if (k < sSize) 
			for (j = k; j < sSize; j++)
				if (s[j] >= g[i]) {
					cnt++;
					k = j + 1;
					break;
				}
	}
	return cnt;
}
