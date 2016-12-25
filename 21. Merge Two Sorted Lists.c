/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *p1 = l1, *p2 = l2, *p, *head;
    if (p1 == NULL)
        return l2;
    else if (p2 == NULL)
        return l1;
    if (p1 -> val <= p2 -> val){
        head = p1;
        p1 = p1 -> next;
    }// first node same with smaller one
    else{
        head = p2;
        p2 = p2 -> next;
    }
    p = head;
    while (p1 != NULL || p2 != NULL){
        if (p1 == NULL){
            p -> next = p2;
            p2 = p2 -> next;
        } // if l1 ends
        else if (p2 == NULL){
            p -> next = p1;
            p1 = p1 -> next;
        }
        else if (p1 -> val <= p2 -> val){
            p -> next = p1;
            p1 = p1 -> next;
        }
        else{
            p -> next = p2;
            p2 = p2 -> next;
        }
        p = p -> next; // p move to the next node
    }
    return head;
}
