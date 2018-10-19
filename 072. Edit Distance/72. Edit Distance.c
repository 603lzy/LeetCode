int minof3(int x, int y, int z){
    int tmp;
    tmp = x > y ? y : x;
    return tmp > z ? z : tmp;
}

int minDistance(char* word1, char* word2) {
    int len1 = strlen(word1), len2 = strlen(word2);
    int dp[len1 + 1][len2 + 1], i, j, cost;
    for (i = 0; i <= len1; i++)
        dp[i][0] = i;
    for (j = 0; j <= len2; j++)
        dp[0][j] = j;
    
    for (i = 1; i <= len1; i++)
        for (j = 1; j <= len2; j++){
            dp[i][j] = minof3(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1] ? 1 : 0));
        }
    return dp[len1][len2];
}
