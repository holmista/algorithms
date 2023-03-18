#include <iostream>
#include "vector"
#include "queue"
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> arr;
    vector<vector<int>> levelOrder(TreeNode* root) {
        bfs(root);
        return arr;
    }
    void bfs(TreeNode *root){
        if (root == nullptr)
            return;
        vector<TreeNode*> q;
        q.push_back(root);
        while(!q.empty()){
            vector<int> locVec;
            for(const auto &elem:q){
                locVec.push_back(elem->val);
            }
            arr.push_back(locVec);
            int numElems = q.size();
            for(int i=0; i<numElems; i++){
                if(q[i]->left)
                    q.push_back(q[i]->left);
                if(q[i]->right)
                    q.push_back(q[i]->right);
            }
            for(int i=0; i<numElems; i++){
                q.erase(q.begin());
            }
            locVec.clear();
        }
    }
};

int main(){
    TreeNode *n1 = new TreeNode(1);
    TreeNode *n2 = new TreeNode(2);
    TreeNode *n3 = new TreeNode(3);
    n1->left = n2;
    n1->right = n3;
    TreeNode *n4 = new TreeNode(4);
    TreeNode *n5 = new TreeNode(5);
    n2->left = n4;
    n2->right = n5;
    Solution sol;
    sol.bfs(n1);
    for(int i=0; i<sol.arr.size(); i++){
        for(int j=0; j<sol.arr[i].size(); j++){
            cout << sol.arr[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
 