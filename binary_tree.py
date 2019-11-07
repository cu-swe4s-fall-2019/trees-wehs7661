import sys


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

def insert(root, key, value=None):
    """
    This function insert a value given a root of a tree or a subtree, 
    which could be a child of other nodes.

    Parameters
    ----------
    root : obj
        An object of Node serving as a root of a tree or a subtree
    key : int or float
        The key to be inserted
    value : could be any data type
        The value corresponding to the inserting key

    Return
    ------
    None
    """
    if root is None:
        root = Node(key, value)
    else:
        if key >= root.key:
            if root.right is None:
                root.right = Node(key, value)
            else:
                # Use root.right as the root of the subtree
                insert(root.right, key, value)
        else:
            if root.left is None:
                root.left = Node(key, value)
            else:
                # Use root.left as the root of the subtree
                insert(root.left, key, value)

def print_tree(root, key_list=[], value_list=[]):
    """
    This function prints key of each node in a tree to a list, from the 
    rightmost node to the leftmost. This function could be useful for 
    checking the functionality of the insert function.

    Parameters
    ----------
    root : obj
        An object of Node serving as a root of a tree or a subtree
    key_list : list
        A list of keys
    value_list : list
        A list of value

    Returns
    -------
    None
    """

    if root is None:
        print('The root of the tree is null!')
        sys.exit()
    else:
        key_list.append(root.key)
        value_list.append(root.value)
        if root.right is not None:
            print_tree(root.right, key_list, value_list)
            # root.right.key will be print out when executing print(root.key)
            # in print_tree(root.right)
        if root.left is not None:
            print_tree(root.left, key_list, value_list)
            # root.left.key will be print out when executing print(root.key)
            # in print_tree(root.left)
            
    return key_list, value_list

def search(root, key):
    if root is None:
        return None
    else:
        if root.key == key:
            return root.value
        elif root.right is None and root.left is None:
            return None
        elif key >= root.key:
            return search(root.right, key)
            # No need to return root.right.value, since this should be
            # returned by root.key as root is replaced by root.right
        elif key < root.key:
            return search(root.left, key)
            # No need to return root.right.value, since this should be
            # returned by root.key as root is replaced by root.right






