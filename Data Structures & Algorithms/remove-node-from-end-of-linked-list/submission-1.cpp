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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        //loop first get length.
        //  k = length-n = index to remove
        //loop k times and remove
            //get curr, get next next, curr = next next
        ListNode* cur = head;
        int len = 0;
        while(cur!=nullptr){
            len++;
            cur = cur->next;
        }
        if(len==1){
            return nullptr;
        }
        int k = len-n; //index to delete from the front
        if(k ==0){
            return head->next;
        }
        //reset cur
        cur = head;
        //move to the one before the node to be removed
        for(int i = 1;i<k;i++){
            cur = cur->next;
        }
        ListNode* save = cur -> next->next;
        std::cout<<save;

        cur->next = save;
        return head;

    }
};
