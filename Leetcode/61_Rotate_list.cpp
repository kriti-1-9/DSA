/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == nullptr) return 0;
        int l = 0;
        ListNode* temp = head;
        while(temp -> next != nullptr) {
            temp = temp -> next;
            l += 1;
        }
        k %= (l+1);
        if(k == 0) return head;
        temp -> next = head;
        for(int i=0; i<l-k+1; i++) {
            temp = temp -> next;
        }
        head = temp -> next;
        temp -> next = nullptr;
        return head;
    }
};