/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* insertionSortList(struct ListNode* head) {
    if (head == NULL || head->next == NULL) {
        return head;
    }
    struct ListNode* sorted = NULL;
    struct ListNode* curr = head;
    while (curr != NULL) {
        struct ListNode* next = curr->next; 
        if (sorted == NULL || sorted->val >= curr->val) {
            curr->next = sorted;
            sorted = curr;
        } else {
            struct ListNode* temp = sorted;
            while (temp->next != NULL && temp->next->val < curr->val) {
                temp = temp->next;
            }
            curr->next = temp->next;
            temp->next = curr;
        }
        curr = next;
    }
    return sorted;
}