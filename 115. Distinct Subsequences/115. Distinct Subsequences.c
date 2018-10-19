//ref: https://discuss.leetcode.com/topic/46346/my-0-ms-dp-solution-in-c-o-mn-time-o-n-space
#define MAXN 1024
int numDistinct(char* s, char* t) {
	const int lens = strlen(s), lent = strlen(t);
	int dp[MAXN] = {1};
	int i, j;

	for (i = 0; i < lens; i++)
		for (j = lent; j >= 0; j--)
			if (t[j] == s[i])
				dp[j + 1] += dp[j];
	return dp[lent];
}
