#include <iostream>
#include "string"
#include <stdexcept>
using namespace std;

struct Node{
    int val;
    struct Node *left;
    struct Node *right;
    struct Node *parent;
};

string repeat_string(string str, int n) {
    string result = "";
    for (int i = 0; i < n; i++) {
        result += str;
    }
    return result;
}

class Bst{
    public:
        Node *root;
        Bst(Node *rootNode){
            root = rootNode;
        }
        void insert(int val, Node *node){
            if(val<=node->val){
                if(node->left == nullptr) {
                    Node *newNode = new Node{val};
                    newNode->parent = node;
                    node->left = newNode;
                }
                else insert(val, node->left);
            } 
            else {
                if(node->right == nullptr) {
                    Node *newNode = new Node{val};
                    newNode->parent = node;
                    node->right = newNode;
                }
                else insert(val, node->right);
            }   
        }
        void remove(int val, Node *node){
            Node *nodeToRemove = dfs(val, root);
            if (nodeToRemove==nullptr) throw invalid_argument("node with that value not found");
            else if(nodeToRemove->left==nullptr && nodeToRemove->right==nullptr){
                if(nodeToRemove->parent->left == nodeToRemove) nodeToRemove->parent->left = nullptr;
                else nodeToRemove->parent->right = nullptr;
            }
            else if(nodeToRemove->left!=nullptr && nodeToRemove->right==nullptr){
                Node *next = nodeToRemove->left;
                if(nodeToRemove->parent->left == nodeToRemove) nodeToRemove->parent->left = next;
                else if (nodeToRemove->parent->right == nodeToRemove) nodeToRemove->parent->right = next;
            }
            else if(nodeToRemove->left==nullptr && nodeToRemove->right!=nullptr){
                Node *next = nodeToRemove->right;
                if(nodeToRemove->parent->left == nodeToRemove) nodeToRemove->parent->left = next;
                else if (nodeToRemove->parent->right == nodeToRemove) nodeToRemove->parent->right = next;
            }
            else{
                // here node to remove has both children, which means that
                // we should go to the right child and then all the way down to the leftmost child
                // we should save that and place it under parent of node to remove
                // left child of left most child's parent should be null
                // the moved child's lefts and rights have to be set
                Node *curr = nodeToRemove->right;
                if(curr->left == nullptr && curr->right==nullptr){
                    curr->parent->right = nullptr;
                    curr->left = nodeToRemove->left;
                    if(nodeToRemove->parent->left == nodeToRemove) nodeToRemove->parent->left = curr;
                    if(nodeToRemove->parent->right == nodeToRemove) nodeToRemove->parent->right = curr;
                    if(1==2) cout << 7;
                }
                else{
                    while(curr->left!=nullptr){
                        curr = curr->left;
                    }
                    Node *leftMostChild = curr;
                    leftMostChild->parent->left = nullptr;
                    leftMostChild->left = nodeToRemove->left;
                    leftMostChild->right = nodeToRemove->right;
                    if(nodeToRemove->parent->left == nodeToRemove) nodeToRemove->parent->left = leftMostChild;
                    if(nodeToRemove->parent->right == nodeToRemove) nodeToRemove->parent->right = leftMostChild;
                }
            }
            delete nodeToRemove;
        }
        Node* dfs(int val, Node *node){
            if(node == nullptr) return nullptr;
            if(node->val == val) return node;
            else if(node->val<val){
                return dfs(val, node->right);
            } 
            else{
                return dfs(val, node->left);
            }   
        }
        void print(Node *node, int indent){
            if(node == nullptr) return;
            string empty = repeat_string("#", indent);
            cout << empty << node->val << endl;
            print(node->left, indent + 1);
            print(node->right, indent + 1);
        }

};

int main(){
    Node node1 = {20};
    Bst *tree = new Bst(&node1);
    tree->insert(10, tree->root);
    tree->insert(7, tree->root);
    tree->insert(18, tree->root);
    tree->insert(16, tree->root);
    tree->insert(15, tree->root);
    tree->insert(5, tree->root);
    tree->insert(9, tree->root);
    tree->remove(10, tree->root);
    tree->print(tree->root, 0);
    // cout << tree->root->left->right->right->val << endl;
    delete tree;
    return 0;
}

//            20
//          /
//         10
//        /   \
//       7    18
//     / \   /
//    5  9 16
//        /
//       15