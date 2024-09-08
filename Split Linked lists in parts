class Solution {
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) 
    {
        vector<ListNode*> node;
        ListNode* curr = head;
        node.push_back(curr);
        int n=0;
        while (curr) {     
            curr=curr->next;
            node.push_back(curr);
            n++;
        }

        auto [q, r]=div(n, k);
       
        vector<int> iLen(k, q);
        fill(iLen.begin(), iLen.begin()+r, q+1);
        vector<ListNode*> ans(k, {});
        int beginIdx=0, endIdx;
        
        //Consider only the heads & tails for ans[i]
        for (int i=0; i<k; i++) {
            beginIdx=(i==0) ? 0:beginIdx+iLen[i-1];
            endIdx=(iLen[i]==0)?beginIdx:beginIdx+iLen[i]-1;
            ans[i]=node[beginIdx];
            ListNode* last = node[endIdx];
            if (last) 
                last->next = NULL; // Remove the link
        }       
        return ans;
    }
};
