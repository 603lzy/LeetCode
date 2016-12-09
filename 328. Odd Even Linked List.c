/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head) {
    //https://discuss.leetcode.com/topic/34289/4ms-c-code-not-perfect-codes-but-clear-codes
  if (head){
    
    struct ListNode* p = head;
    struct ListNode* q = head->next;
    struct ListNode* temp = q;
    
    while(p->next && q->next){
        p -> next = q->next;
        p = p->next;
        
        q -> next = p -> next;
        q = q->next;
    }
    p -> next = temp;
    }
    return head;
}
