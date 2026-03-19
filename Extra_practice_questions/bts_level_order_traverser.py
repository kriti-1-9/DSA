# Problem Statement:

"""
You are given an array nums of integers of length n that represents the inorder traversal of a balanced binary search tree (BST). Your task is to construct this BST from the given array and return its level order serialization.

A balanced BST is a tree in which the depth difference between the two subtrees of any node is not more than 1. If there are multiple possible balanced BSTs based on the given array, you should construct the tree that has more nodes as a left child than as a right child.

Note: nums is sorted in a strictly increasing order and 'null' values of level order serialization are not included in the final output.

Input Format
The first line of input contains N representing the number of nodes in the BST.

The second line of input contains N integers , separated by space, representing the inorder traversal of the required balanced BST.

Output Format
Output a string representing the level order serialization of the constructed BST, where 'null' values are not included.

Constraints
1 <= n <= 10^4

-10^4 <= nums[i] <= 10^4

 

Sample Testcase 0
Testcase Input
20
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9
Testcase Output
-1 -6 4 -9 -4 1 7 -10 -8 -5 -3 0 2 5 8 -7 -2 3 6 9
Explanation
The input is an inorder traversal of a balanced BST. The middle element of the sorted array will be the root of the BST. The left half of the array will be the left subtree, and the right half will be the right subtree. This process is repeated recursively for each half.




-1 -6 4 -9 -4 1 7 -10 -8 -5 -3 0 2 5 8 -7 -2 3 6 9, is an level order traversal of the balanced bst.

Sample Testcase 1
Testcase Input
7
1 2 3 4 5 6 7
Testcase Output
4 2 6 1 3 5 7
Explanation
The input is an inorder traversal of a balanced BST. The middle element of the sorted array will be the root of the BST. The left half of the array will be the left subtree, and the right half will be the right subtree. This process is repeated recursively for each half.


The constructed BST is as follows:

The level order serialization of this BST is "4 2 6 1 3 5 7".
"""

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    def Build(left, right):
        if left > right:
            return None

        mid = (left + right) // 2

        if((right - left + 1) % 2 == 0):
            mid = (left + right - 1) // 2

        root = TreeNode(nums[mid])
        root.left = Build(left, mid - 1)
        root.right = Build(mid + 1, right)

        return root
    return Build(0, len(nums) - 1)
        

def treeNodeToString(root):
    if not root:
        return ""
    
    output = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        output.append(str(node.val))

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return " ".join(output)