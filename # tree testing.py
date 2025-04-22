# tree testing
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        iolist = []
        def inorderHelper(root):
            if root == None:
                return None
            else:
                inorderTraversal(root.left())
                iolist.append(root.val)
                inorderTraversal(root.right())
        inorderHelper(root)
        return iolist
    

class main():
    root = [1,2,3,4,5,None,8,None,None,6,7,9]
    print(Solution(root))