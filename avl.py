class Node:
    def __init__(self, key, value=None, left=None, right=None):
        """
        Initialization of a node of a tree

        Parameters
        ----------
        key : int or float
            The key of the node
        value : could be any data type
            The value corresponding to the key
        left : obj
            An object of Node serving as the left child of the node
        right : obj
            An object of Node serving as the right child of the node
        """
        self.value = value    # which is None here (default)
        self.left = left      # which is None here (default)
        self.right = right    # which is None here (default)
        self.key = key

class AVLTree():
    def __init__(self):
        """
        Initializing function for an AVL tree
        """
        self.node = None
        self.height = -1   # height = -1 for null child nodes
        self.balance = 0   # balance factor = h(left) - h(right)

    def insert(self, key, value=None):
        """
        This function insert a value given a root of a tree or a subtree, 
        which could be a child of other nodes.

        Parameters
        ----------
        key : int or float
            The key to be inserted
        value : could be any data type
            The value corresponding to the inserting key

        Return
        ------
        None
        """
        n = Node(key, value)

        if self.node is None:
            self.node = n
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        else:
            if key >= self.node.key:
                if self.node.right is None:
                    self.node.right = Node(key, value)
                else:
                    self.node.right.insert(key, value)
            else:
                if self.node.left is None:
                    self.node.left = Node(key, value)
                else:
                    self.node.left.insert(key, value)
        self.rebalance()   # rebalance the tree if needed

    def update_tree_info(self, recursive=True):
        """
        This function updates the information of an AVL tree, including the heights
        and the balance factor of each node.

        Parameters
        ----------
        recursive : bool
            Whether to recursively update the tree information

        Returns
        -------
        None
        """
        if self.node is None:
            self.height = -1
            self.balance = 0
        else:
            if recursive is True:
                if self.node.right is not None:
                    self.node.right.update_tree_info()
                if self.node.left is not None:
                    self.node.left.update_tree_info()
            self.height = 1 + max(self.node.left.height, self.node.right.height)
            self.balance = self.node.left.height - self.node.right.height

    def rotate_right(self):
        """
        This function implements a right rotation on a node.
        """
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        """
        This function implements a left rotation on a node.
        """
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def rebalance(self):
        """
        This function rebalance an AVL tree through rotations.
        """
        # get the info but do not update yet
        self.update_tree_info(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance < -1:   # right subtree is larger
                if self.node.right.balance > 0:
                    # right left
                    self.node.right.rotate_right()
                    self.update_tree_info()
                #right right
                self.rotate_left()
                self.update_tree_info()
            if self.balance > 1:    # left subtree is larger
                if self.node.left.balance < 0:
                    # left right
                    self.node.left.rotate_left()
                    self.update_tree_info()
                # left left
                self.rotate_right()
                self.update_tree_info()

    def search(self, key):
        """
        This function takes in a key and returns its corresponding value.

        Parameters
        ----------
        key : int or float
            The key to be looked for

        Returns
        -------
        The value corresponds to the given key. 
        """
        if self.node is None:
            return None
        else:
            if self.node.key == key:
                return self.node.value
            elif self.node.right is None and self.node.left is None:
                return None
            elif key >= self.node.key:
                return self.node.right.search(key)
            elif key < self.node.key:
                return self.node.left.search(key)