//wrong answer!!!

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
    	ListNode *l3 = NULL;
    	ListNode *temp = NULL;
    	int flag = 0;

    	while(l1!=NULL&&l2!=NULL){

    		temp = new ListNode(l1->val + l2->val);
    		
    		temp->next = l3;
    		l3 = temp;

    		l1 = l1->next;
    		l2 = l2->next;
    	}

       	if(l1==NULL&&l2!=NULL){
    		temp = new ListNode(l2->val);
    		temp->next = l3;
    		l3 = temp;
    		l2 = l2->next;
    	}else if(l2==NULL&&l1!=NULL){
    		temp = new ListNode(l1->val);
    		temp->next = l3;
    		l3 = temp;
    		l1 = l1->next;
    	}

    	ListNode *p = l3;
    	while(l3!=NULL){
    	/*	if(p->val+flag>=10){
    			flag = 1;
    			p->val = flag+p->val-10;
    		}else{
    			flag = 0;
    			p->val = flag+p->val;
    		}*/
    	}
/*
    	if(p->val+flag<10){
    		p->val = flag + p->val;
    	}else{
    		p->val = flag + p->val -10;
    		temp = new ListNode(1);
    		temp->next = NULL;
    		p->next = temp;
    	}*/


    	return l3;
        
    }
};