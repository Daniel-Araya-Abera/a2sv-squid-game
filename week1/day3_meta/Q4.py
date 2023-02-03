# Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = collections.defaultdict(list)
        queue = deque([(root, 0, 0)])
        while queue:
            curr_node, curr_i, curr_j = queue.popleft()
            # columns[curr_j].append((curr_node.val))
            columns[curr_j].append((curr_i, curr_node.val))
            if curr_node.left:
                queue.append((curr_node.left, curr_i + 1, curr_j - 1))
            if curr_node.right:
                queue.append((curr_node.right, curr_i + 1, curr_j + 1))
        
        res = []
        
        column_indices = sorted(columns.keys())
        for col_idx in column_indices:
            curr_res = []
            col_items = sorted(columns[col_idx])
            for _, node_val in col_items:
                curr_res.append(node_val)
            res.append(curr_res)
        return res
