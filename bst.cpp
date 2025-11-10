#include <iostream>
#include <vector>
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

Node* insert(Node* root, int val) {
    if(root == NULL) {
        return new Node(val);
    }

    if(val < root->data) {
        root->left = insert(root->left, val);
    } else {
        root->right = insert(root->right, val);
    }

    return root;
}

Node* buildBST(vector<int> arr) {
    Node* root = NULL;

    for(int val : arr) {
        root = insert(root, val);
    }

    return root;
}

void inorder(Node* root) {
    if(root == NULL) {
        return;
    }

    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

bool search(Node* root, int key) {
    if(root == NULL) {
        return false;
    }

    if(root->data == key) {
        return true;
    }

    if(key < root->data) {
        return search(root->left, key);
    } else {
        return search(root->right, key);
    }
}

Node* getInorderSuccessor(Node* root) {
    while(root != NULL && root->left != NULL) {
        root = root->left;
    }
    return root;
}

Node* delNode(Node* root, int key) { // key => val to delete
    if(root == NULL) {
        return NULL;
    }

    if(key < root->data) {
        root->left = delNode(root->left, key);
    } else if(key > root->data) {
        root->right = delNode(root->right, key);
    } else {
        if(root->left == NULL) {
            Node* temp = root->right;
            delete root;
            return temp;
        } else if(root->right == NULL) {
            Node* temp = root->left;
            delete root;
            return temp;
        } else { // 2 children
            Node* IS = getInorderSuccessor(root->right);
            root->data = IS->data;
            root->right = delNode(root->right, IS->data);
        }
    }
}

Node* buildBSTFromSorted(const vector<int>& arr, int start, int end) {
    if(start > end) {
        return NULL;
    }

    int mid = start + (end - start) / 2;
    Node* root = new Node(arr[mid]);
    root->left = buildBSTFromSorted(arr, start, mid - 1);
    root->right = buildBSTFromSorted(arr, mid + 1, end);

    return root;
}

Node* merge2BST(Node* root1, Node* root2) {
    vector<int> arr1, arr2;
    inorder(root1, arr1);
    inorder(root2, arr2);

    vector<int> temp;

    int i = 0, j = 0;
    while(i < arr1.size() && j < arr2.size()) {
        if(arr1[i] < arr2[j]) {
            temp.push_back(arr1[i++]);
        } else {
            temp.push_back(arr2[j++]);
        }
    }

    while(i < arr1.size()) {
        temp.push_back(arr1[i++]);
    }
    while(j < arr2.size()) {
        temp.push_back(arr2[j++]);
    }

    return buildBSTFromSorted(temp, 0, temp.size() - 1);
}

int main() {
    vector<int> arr1 = {8, 2, 1, 10};
    vector<int> arr2 = {5, 3, 0};

    Node* root1 = builBST(arr1);
    Node* root2 = builBST(arr2);

    Node* root = merge2BST(root1, root2);
    vector<int> seq;
    inorder(root, seq);
    for(int val : seq) {
        cout << val << " ";
    }
    cout << endl;
    
    // vector<int> arr = {3, 2, 1, 5, 6, 4};

    // Node* root = buildBST(arr);

    // cout << "before: ";
    // inorder(root);
    // cout << endl;

    // delNode(root, 6);

    // cout << "after: ";
    // inorder(root);
    // cout << endl;

    // cout << search(root, 5) << endl;

    // inorder(root);
    // cout << endl;

    return 0;
}