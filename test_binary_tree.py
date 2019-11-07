import binary_tree as bt
import unittest

class TestBinaryTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
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

    def test_insert(self):
        self.assertEqual([self.root.key, self.root.value], [6, 'Root'])
        self.assertEqual([self.root.left.key, self.root.left.value], [3, 'D'])
        self.assertEqual([self.root.right.key, self.root.right.value], [7, 'A'])
        self.assertEqual([self.root.left.left.key, self.root.left.left.value], [2, 'E'])

    def test_print_tree(self):
        key_list, value_list = bt.print_tree(self.root)
        self.assertEqual(key_list, [6, 7, 8, 9, 3, 4, 5, 2])
        self.assertEqual(value_list, ['Root', 'A', 'B', 'C', 'D', 'F', 'G', 'E'])

    def test_search(self):
        r0 = bt.search(self.root, 6)
        r1 = bt.search(self.root, 2)
        r2 = bt.search(self.root, 8)
        r3 = bt.search(self.root, 7.5)
        self.assertEqual(r0, 'Root')
        self.assertEqual(r1, 'E')
        self.assertEqual(r2, 'B')
        self.assertEqual(r3, None)

if __name__ == '__main__':
    unittest.main()

        