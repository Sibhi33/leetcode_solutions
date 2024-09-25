struct Node{
    unordered_map<char,pair<int,Node*>> umc;
    bool is_end=false;
};

class Trie{
private:
    Node *root;
public:
    // constructor always gets called when class is called
    // help us to always keep track of first head node
    Trie(){
        root = new Node();
    }

    // insertion function
    void insert(string s){
        Node *cur = root;
        for(int i=0;i<s.size();i++){
            if(cur->umc.find(s[i]) == cur->umc.end()){
                cur->umc[s[i]].second = new Node();
            }

            cur->umc[s[i]].first++;
            cur = cur->umc[s[i]].second;
        }

        cur->is_end = true;
        return;
    }

    // function to match the prefix
    int check_prefix_count(string s){
        Node *cur = root;
        int count = 0;

        for(int i=0;i<s.size();i++){
            if(cur->umc.find(s[i]) == cur->umc.end()){
                break;
            }

            count += cur->umc[s[i]].first;
            cur = cur->umc[s[i]].second;
        }
         
        return count;
    }
};

class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        Trie t; // initiate trie

        for(auto &word:words){ // for(int i=0;i<words.size();i++)
            t.insert(word); // word = words[i]
        }

        vector<int> ans;
        for(auto &word:words){ 
            int tmp = t.check_prefix_count(word); 
            ans.push_back(tmp);
        }

        return ans;
    }
};
