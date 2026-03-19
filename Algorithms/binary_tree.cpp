#include <iostream>
#include <vector>
#include <queue>
#include <map>
using namespace std;

class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};

static int idx = -1;
Node* buildTree(vector<int> preorder) {
    idx++;

    if(preorder[idx] == -1) {
        return NULL;
    }

    Node* root = new Node(preorder[idx]);
    root->left = buildTree(preorder);
    root->right = buildTree(preorder);

    return root;
}

//preorder
void preOrder(Node* root) {
    if(root == NULL) {
        return;
    }

    cout << root->data << " ";
    preOrder(root->left);
    preOrder(root->right);
}

void inorder(Node* root) {
    if(root == NULL) {
        return;
    }

    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

//postorder
void postOrder(Node* root) {
    if(root == NULL) {
        return ;
    }

    postOrder(root->left);
    postOrder(root->right);
    cout << root->data << " ";
}

//level order
void levelOrder(Node* root) {
    queue<Node*> q;

    q.push(root);
    q.push(NULL);

    while(q.size() > 0) {
        Node* curr = q.front();
        q.pop();

        if(curr == NULL) {
            if(!q.empty()) {
                cout << endl;
                q.push(NULL);
                continue;
            } else {
                break;
            }
        }

        cout << curr->data << " ";

        if(curr->left != NULL) {
            q.push(curr->left);
        }
        if(curr->right != NULL) {
            q.push(curr->right);
        }
    }
    cout << endl;
}

int height(Node* root) {
    if(root == NULL) {
        return 0;
    }

    int leftHt = height(root->left);
    int rightHt = height(root->right);
    return max(leftHt, rightHt) + 1;
}

// count Nodes
int count(Node* root) {
    if(root == NULL) {
        return 0;
    }

    int leftCount = count(root->left);
    int rightCount = count(root->right);
    return leftCount + rightCount + 1;
}

int sumOfNodes(Node* root) {
    if(root == NULL) {
        return 0;
    }

    int leftSum = sumOfNodes(root->left);
    int rightSum = sumOfNodes(root->right);
    return leftSum + rightSum + root->data;
}

void topView(Node* root) {
    queue<pair<Node*, int>> q;
    map<int, int> m;
    q.push({root, 0});

    while(q.size() > 0) {
        Node* curr = q.front().first;
        int currHD = q.front().second;
        q.pop();

        if(m.find(currHD) == m.end()) {
            m[currHD] = curr->data;
        }

        if(curr->left != NULL) {
            q.push({curr->left, currHD-1});
        }

        if(curr->right != NULL) {
            q.push({curr->right, currHD+1});
        }
    }

    for(auto it : m) {
        cout << it.second << " ";
    }

    cout << endl;
}

void KthLevel(Node* root, int K) {
    if(root == NULL) {
        return;
    }

    if(K == 1) {
        cout << root->data << " ";
        return;
    }

    KthLevel(root->left, K-1);
    KthLevel(root->right, K-1);
}

int sumTree(Node* root) {
    if(root == NULL) {
        return 0;
    }

    int leftSum = sumTree(root->left);
    int rightSum = sumTree(root->right);

    root->data += leftSum +rightSum;
    return root->data;
}

int main() {
    vector<int> preorder = {1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1};
    Node* root = buildTree(preorder);

    // KthLevel(root, 3);

    // topView(root);

    // cout << "sum : " <<sumOfNodes(root) << endl;

    // cout << "count : " << count(root) << endl;

    // cout << root->data << endl;

    // cout << "height : " << height(root) << endl;

    // preOrder(root);
    // cout << endl;

    // inorder(root);
    // cout << endl;

    // postOrder(root);
    // cout << endl;

    // levelOrder(root);

    return 0;
}