/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *fp = head, *sp = head; //use two pointers
        for (int i = 0; i < n; i++)
            fp = fp -> next;
        if (fp == NULL)
            return head -> next;
        while (fp -> next != NULL){
            fp = fp -> next;
            sp = sp -> next;
        }
        sp -> next = sp -> next -> next;
        return head;
    }
};
