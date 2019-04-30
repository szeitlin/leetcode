#following example here: http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html

class TreeNode:

    def __init__(self, key,val,left=None,right=None,parent=None):
        self.key = key
        self.val = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def isLeftChild(self):
        return self.parent and self.parent.left_child == self

    def isRightChild(self):
        return self.parent and self.parent.right_child == self

    def isRoot(self):
        return not self.parent #todo: look this up, I don't get this one

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    #skipping replace node data since I don't think I need it for this

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size #why do any of this when you can just check the size attribute?

    def _put(self, key, val, currentNode): #where does currentNode get defined?
        if key < currentNode.key:
            if currentNode.left_child is not None:
                self._put(key,val,currentNode.left_child)
            else:
                currentNode.left_child = TreeNode(key,val, parent=currentNode)
        else:
            if currentNode.right_child is not None:
                self._put(key,val,currentNode.right_child)
            else:
                currentNode.right_child = TreeNode(key,val,parent=currentNode)

    def add_node(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1

    def findSuccessor(self):
        """
        recursive depth-first search
        """
        succ = None
        if self.right_child is not None: #how does this work? BST doesn't inherit-?
            succ = self.right_child.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.findSuccessor()
                    self.parent.right_child = self
        return succ

    def findMin(self):
        current = self
        while current.left_child is not None:
            current = current.left_child
        return current
