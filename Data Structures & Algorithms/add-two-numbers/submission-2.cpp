//COME BACK: an iterative method is better (adding at every node) because my way might cause 
//integer overflow. 

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        //Sum up two list first by timing each index further by 10 more so use
        //10 to the power of index i: ith * 10**i
        int first = 0;
        int second = 0;
        //use to idnex i
        int counter = 0;

        ListNode* cur = l1;

        //sum up l1
        while(cur!=NULL){
            first = first + (cur->val)*std::pow(10,counter);
            counter++;
            cur = cur->next;
        }
        cur = l2;
        counter= 0;
        //sum up l2
        while(cur!=NULL){
            second = second + (cur->val)*std::pow(10,counter);
            counter++;
            cur = cur->next;
        }
        ListNode* dummy = new ListNode(0);
        ListNode* res = dummy;

        int sum = first+second;
        if(sum==0) return new ListNode(0);
        //variable to store each extracted digit from sum
        int store;
        while (sum!=0)
        {
            store = sum%10;
            res->next = new ListNode(store);

            //iterator
            res = res->next;
            sum = sum/10;
            
        }
        return dummy->next;
    }
};
