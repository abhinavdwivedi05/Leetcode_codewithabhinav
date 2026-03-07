class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            node_p, node_q = stack.pop()
            if node_p is None and node_q is None:
                continue
            if node_p is None or node_q is None:
                return False
            if node_p.val != node_q.val:
                return False
            stack.append((node_p.left, node_q.left))
            stack.append((node_p.right, node_q.right))
        return True