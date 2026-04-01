/* Tree node structure  used in the program

struct Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};*/

struct NodeInfo {
    int size;
    int minVal;
    int maxVal;
    bool isBST;
};

class Solution {
public:
    int maxSize = 0;

    NodeInfo solve(Node* root) {
        if (!root) {
            return {0, INT_MAX, INT_MIN, true};
        }

        auto left = solve(root->left);
        auto right = solve(root->right);

        NodeInfo curr;

        // If current subtree is BST
        if (left.isBST && right.isBST &&
            root->data > left.maxVal &&
            root->data < right.minVal) {

            curr.isBST = true;
            curr.size = left.size + right.size + 1;

            curr.minVal = min(root->data, left.minVal);
            curr.maxVal = max(root->data, right.maxVal);
        } 
        else {
            curr.isBST = false;

            curr.size = max(left.size, right.size);

            curr.minVal = INT_MIN;
            curr.maxVal = INT_MAX;
        }

        return curr;
    }

    int largestBst(Node *root) {
        return solve(root).size;
    }
};