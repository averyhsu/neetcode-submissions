/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        //Issue: I can't create random withot having a normal link list established first.
        Node* cur = head;
        Node dummy(0);
        Node* copy = &dummy;
        std::unordered_map<Node*, Node*> nodeMap;

        while(cur!=NULL){
            //create just the linked list
            copy -> next = new Node(cur->val);

            //in hashmap, save current old node as keys to new current node as values
            //so when I traverse the second time and check what the random is I
            // can instantly find what the random should be in new list
            nodeMap[cur] = copy->next;
            //increment  
            cur = cur-> next;
            copy = copy->next;
        }
        //reset cur and cop
        cur = head;
        copy = dummy.next;

        while(cur!=NULL){
            //create just the linked list
            copy ->random = nodeMap[cur->random];
            
            cur = cur-> next;
            copy = copy->next;
        }
        return dummy.next;
    }
};
