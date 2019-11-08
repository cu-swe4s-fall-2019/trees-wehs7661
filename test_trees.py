import binary_tree as bt
import avl
import unittest


class TestBinaryTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        A function for initializing a binary tree for testing.
        """
        cls.root = bt.Node(6, 'Root')
        bt.insert(cls.root, 7, 'A')
        bt.insert(cls.root, 8, 'B')
        bt.insert(cls.root, 9, 'C')
        bt.insert(cls.root, 3, 'D')
        bt.insert(cls.root, 2, 'E')
        bt.insert(cls.root, 4, 'F')
        bt.insert(cls.root, 5, 'G')
        #             _6_
        #            /   \
        #           3     7
        #          / \     \
        #         2   4     8
        #              \     \
        #               5     9

    def test_binary_insert(self):
        """
        An unit test to test the insersion method for a binary tree.
        """
        self.assertEqual([self.root.key, self.root.value], [6, 'Root'])
        self.assertEqual([self.root.left.key, self.root.left.value], [3, 'D'])
        self.assertEqual(
            [self.root.right.key, self.root.right.value], [7, 'A'])
        self.assertEqual(
            [self.root.left.left.key, self.root.left.left.value], [2, 'E'])

    def test_print_tree(self):
        """
        An unit test to test the printing method for a binary tree.
        """
        key_list, value_list = bt.print_tree(self.root)
        self.assertEqual(key_list, [6, 7, 8, 9, 3, 4, 5, 2])
        self.assertEqual(
            value_list, ['Root', 'A', 'B', 'C', 'D', 'F', 'G', 'E'])

    def test_binary_search(self):
        """
        An unit test to test the searching method fora binary tree.
        """
        r0 = bt.search(self.root, 6)
        r1 = bt.search(self.root, 2)
        r2 = bt.search(self.root, 8)
        r3 = bt.search(self.root, 7.5)
        self.assertEqual(r0, 'Root')
        self.assertEqual(r1, 'E')
        self.assertEqual(r2, 'B')
        self.assertEqual(r3, None)


class TestAVLTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        An function for initializing an AVL tree.
        """
        cls.tree = avl.AVLTree()
        cls.tree.insert(1, 'A')
        cls.tree.insert(2, 'B')
        cls.tree.insert(3, 'C')
        # At this point, the tree should be:
        #         _2_
        #        /   \
        #       1     3
        cls.tree.insert(4, 'D')
        cls.tree.insert(5, 'E')
        # At this point, the tree should be:
        #       ___2___
        #      /       \
        #     1        _4_
        #             /   \
        #            3     5
        cls.tree.insert(6, 'F')
        # The result should be:
        #       ___4___
        #      /       \
        #    _2_        5
        #   /   \        \
        #  1     3        6

    def test_avl_insert(self):
        """
        An unit test to test the insertion method for an AVL tree.
        """
        # check the keys
        self.assertEqual(self.tree.node.key, 4)
        self.assertEqual(self.tree.node.right.node.key, 5)
        self.assertEqual(self.tree.node.right.node.right.node.key, 6)
        self.assertEqual(self.tree.node.left.node.key, 2)
        self.assertEqual(self.tree.node.left.node.left.node.key, 1)
        self.assertEqual(self.tree.node.left.node.right.node.key, 3)

        # check the values
        self.assertEqual(self.tree.node.value, 'D')
        self.assertEqual(self.tree.node.right.node.value, 'E')
        self.assertEqual(self.tree.node.right.node.right.node.value, 'F')
        self.assertEqual(self.tree.node.left.node.value, 'B')
        self.assertEqual(self.tree.node.left.node.left.node.value, 'A')
        self.assertEqual(self.tree.node.left.node.right.node.value, 'C')

    def test_avl_search(self):
        """
        An unit test to test the searching method for an AVL tree.
        """
        r0 = self.tree.search(4)
        r1 = self.tree.search(6)
        r2 = self.tree.search(3)
        r3 = self.tree.search(4.5)
        self.assertEqual(r0, 'D')
        self.assertEqual(r1, 'F')
        self.assertEqual(r2, 'C')
        self.assertEqual(r3, None)


if __name__ == '__main__':
    unittest.main()
