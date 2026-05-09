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
    void reorderList(ListNode* head) {
       
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast->next!=nullptr &&fast->next->next!=nullptr)
        {
            slow =  slow->next;
            fast = fast->next->next;
        }
        if(slow==head) return;

        ListNode* second_head = slow->next;
        slow -> next = nullptr;
        //flip second head
        ListNode* tmp = nullptr;
        ListNode* cur;
        while(second_head){
            cur = second_head;
            second_head = second_head->next;
            cur ->next = tmp;
            tmp = cur;
        }
        ListNode dummy(0);
        ListNode* start = &dummy;
        int i =0;
        while(cur){
            if(i%2==0){
                start -> next = head;
                head = head->next;
            }
            else{
                start -> next = cur;
                cur = cur -> next;
            }
            start = start -> next;
            i++;
        }
        if(head) start -> next = head;

        head = dummy.next;

    

    }
};
