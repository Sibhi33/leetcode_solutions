class Solution {
public:
    static int findTheWinner(int n, int k) {
        if (n==1) return 1;
        if (k==1) return n;// special case
        queue<int> q;
        for(int i=1; i<=n; i++){
            if (i%k==0) continue;
            q.push(i);
        }
        int k0=(k-n%k)%n;//Next one should be removed
    //    cout<<k0<<endl;
        for(int i=1; i<k0; i++){
            q.pop();
            q.push(i);
        }
        //a full circular transversal is through, may obtain the answer
        if (q.size()==1) return q.front();
        q.pop();

        while(q.size()>1){
           for (int i= 0; i<k-1; i++) {
                q.push(q.front());
                q.pop();
            }
            // Remove the k-th element
            q.pop();
        }

        return q.front();
    }
};
