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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *result = new ListNode(0);
        ListNode *cursor = result;
        int carry = 0;
        while (l1 && l2) {
            cursor->val = (l1->val + l2->val + carry) % 10;
            carry = (l1->val + l2->val + carry) / 10;
            if (l1->next && l2->next) {
                cursor->next = new ListNode(0);
                cursor = cursor->next;
            }
            l1 = l1->next;
            l2 = l2->next;
        }
        while (l1) {
            cursor->next = new ListNode(0);
            cursor = cursor->next;
            cursor->val = (l1->val + carry) % 10;
            carry = (l1->val + carry) / 10;
            l1 = l1->next;
        }
        while (l2) {
            cursor->next = new ListNode(0);
            cursor = cursor->next;
            cursor->val = (l2->val + carry) % 10;
            carry = (l2->val + carry) / 10;
            l2 = l2->next;
        }
        if (carry) {
            cursor->next = new ListNode(carry);
        }
        return result;
    }
};
