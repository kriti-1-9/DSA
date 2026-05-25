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
    ListNode* mergeTwo(ListNode* head1, ListNode* head2) {
        ListNode* dummy = new ListNode(-1);
        ListNode* curr = dummy;
        while(head1 != nullptr && head2 != nullptr) {
            if(head1 -> val <= head2 -> val) {
                curr -> next = head1;
                head1 = head1 -> next;
            } else {
                curr -> next = head2;
                head2 = head2 -> next;
            }
            curr = curr -> next;
        }
        if(head1 != nullptr) {
            curr -> next = head1;
        } else {
            curr -> next = head2;
        }
        return dummy -> next;
    }

    ListNode* mergeListsRecur(int i, int j, vector<ListNode*> &arr) {
        if(i == j) return arr[i];
        int mid = i + (j - i) / 2;
        ListNode* head1 = mergeListsRecur(i, mid, arr);
        ListNode* head2 = mergeListsRecur(mid+1, j, arr);
        ListNode* head = mergeTwo(head1, head2);
        return head;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size() == 0) return nullptr;
        return mergeListsRecur(0, lists.size()-1, lists);
    }
};