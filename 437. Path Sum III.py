/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 * https://leetcode.com/problems/path-sum-iii/
 */
int sumUp(struct TreeNode* root, int pre, int sum){
    if (!root)
        return 0;
    int current = pre + root -> val;
    return (current == sum) + sumUp(root -> left, current, sum) + sumUp(root -> right, current, sum);
}
 
int pathSum(struct TreeNode* root, int sum) {
    if(!root)
        return 0;
    return sumUp(root, 0, sum) + pathSum(root -> left, sum) + pathSum(root -> right, sum);
}
