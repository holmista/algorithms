#include <iostream>
#include "vector" 
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
    vector<vector<int>> nums;
    vector<int> rightSideView(TreeNode* root) {
        bfs(root);
        vector<int> rightView;
        for(int i=0; i<nums.size(); i++){
            rightView.push_back(nums[i][nums[i].size()-1]);
        }
        return rightView;
    }
    void bfs(TreeNode *root){
        if(root == nullptr) return;
        vector<int> locVec;
        vector<TreeNode*> q;
        q.push_back(root);
        while(!q.empty()){
            vector<int> locVec;
            for(int i=0; i<q.size(); i++){
                locVec.push_back(q[i]->val);
            }
            nums.push_back(locVec);
            int len = q.size();
            for(int i=0; i<len; i++){
                if(q[i]->left)
                    q.push_back(q[i]->left);
                if(q[i]->right)
                    q.push_back(q[i]->right);
            }
            for(int i=0; i<len; i++){
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
    auto res = sol.rightSideView(n1);
    for(int i=0; i<res.size(); i++)
        cout << res[i] << " ";
    return 0;
}