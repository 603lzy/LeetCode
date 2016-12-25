/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode *fp = head, *sp = head;
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
