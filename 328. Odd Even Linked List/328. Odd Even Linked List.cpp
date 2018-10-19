/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * https://discuss.leetcode.com/topic/34837/simple-c-solution-o-n-time-o-1-space
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (!head)
            return head;
        ListNode* po = head, *ehead = head -> next, *pe = ehead;
        while(pe && pe -> next){
            po -> next = po -> next -> next;
            pe -> next = pe -> next -> next;
            po = po -> next;
            pe = pe -> next;
        }
        po -> next = ehead;
        return head;
    }
 
};
