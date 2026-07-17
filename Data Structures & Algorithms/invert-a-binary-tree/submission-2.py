# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #we start with the root
        dests = [root]
        start = root
        while dests:
            #look at the top of the stack
            topDest = dests.pop()
            if not topDest:
                break
            #do your logic here
            temp = topDest.left
            topDest.left = topDest.right
            topDest.right = temp

            # add nodes to destination stack if they exist
            if topDest.left:
                dests.append(topDest.left)
            if topDest.right:
                dests.append(topDest.right)
            #we remove whatever node we're on from the
            #list since we've completed traversing it
        return start

        """how can I reach a leaf, while keeping track of each node
        i've travelled to? I could use a hashset, but then how could
        i look at that hashset to see ones that I haven't dests
        whenever I go to a node, do I just store the left and right
        nodes into the hashset? I could use a stack. The order that 
        we traverse the nodes in doesn't seem to make a difference as
        long as each one is reached and inverted.
        """
