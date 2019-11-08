import os
import sys
import time
import argparse
import binary_tree as bt
sys.path.insert(1, 'hash-tables-wehs7661')   # noqa: E402
sys.path.insert(2, 'avl_tree')               # noqa: E402
import avl
import hash_tables
import hash_functions


def initialize():
    """
    An initializing function

    Parameters
    ----------
    No parameters required

    Return
    ------
    args_parse : namespace
        a namespace containing the argument parser
    """

    parser = argparse.ArgumentParser(
        description='This code'
    )
    parser.add_argument('-d',
                        '--data_structure',
                        type=str,
                        choices=['hash', 'AVL', 'tree', 'all'],
                        help='The data structure to be used.',
                        required=True)
    parser.add_argument('-i',
                        '--dataset',
                        type=str,
                        choices=['rand.txt', 'sorted.txt'],
                        help='The dataset to be used.',
                        required=True)
    parser.add_argument('-n',
                        '--number_pairs',
                        type=int,
                        default=10000,
                        help='The number of data (key/value pairs) to be \
                        inserted/search in the selected data structure',
                        required=False)

    args_parse = parser.parse_args()

    return args_parse


def main():
    args = initialize()

    if args.number_pairs <= 1 or args.number_pairs > 10000:
        print('The number of key/value pairs should be in the range of 2 to 10000.')
        sys.exit(1)

    if not os.path.exists(args.dataset):
        print('Input dataset not found.')
        sys.exit(1)
    else:
        f = open(args.dataset, 'r')
        lines = f.readlines()
        f.close()

    if args.data_structure == 'hash' or args.data_structure == 'all':
        print('\nResults of the hash table')
        print('=========================')
        # key insertion
        table = hash_tables.ChainedHash(10 * int(args.number_pairs), hash_functions.h_rolling)
        i = 0     # number of pairs taken in / line number
        key_list = []
        start = time.time()
        for l in lines:
            key = l.split(' ')[0]
            value = l.split(' ')[1]
            key_list.append(key)
            if i < args.number_pairs:
                table.add(key, value)
                i += 1
            else:
                break
        end = time.time()
        print('It requires %8.7f seconds to insert %s keys to the hash table.' %((end - start), args.number_pairs))

        # searching existing keys
        start = time.time()
        for key in key_list:
            table.search(key)
        end = time.time()
        print('It requires %8.7f seconds to search for all the %s keys inerted just now in the hash table.' %((end - start), args.number_pairs))

        # searching non-existing keys
        start = time.time()
        for key in key_list:
            table.search(key + '_non')
        end = time.time()
        print('It requires %8.7f seconds to search for %s non-existing keys in the hash table.\n' %((end - start), args.number_pairs))

    if args.data_structure == 'AVL' or args.data_structure == 'all':
        print('Results of the AVL tree')
        print('=======================')
        # key insertion
        avl_tree = avl.AVLTree()
        i = 0     # number of pairs taken in / line number
        key_list = []
        start = time.time()
        for l in lines:
            key = l.split(' ')[0]
            value = l.split(' ')[1]
            key_list.append(key)
            if i < args.number_pairs:
                avl_tree.insert(key, value)
                i += 1
        end = time.time()
        print('It requires %8.7f seconds to insert %s keys to the AVL tree.' %((end - start), args.number_pairs))

        # searching existing keys
        start = time.time()
        for key in key_list:
            avl_tree.search(key)
        end = time.time()
        print('It requires %8.7f seconds to search for all the %s keys inerted just now in the AVL tree.' %((end - start), args.number_pairs))

        # searching non-existing keys
        start = time.time()
        for key in key_list:
            avl_tree.search(key + '_non')
        end = time.time()
        print('It requires %8.7f seconds to search for %s non-existing keys in the AVL tree.\n' %((end - start), args.number_pairs))


    if args.data_structure == 'tree' or args.data_structure == 'all':
        print('Results of the binary tree')
        print('==========================')
        # key insertion
        i = 0     # number of pairs taken in / line number
        key_list = []
        start = time.time()
        for l in lines:
            key = l.split(' ')[0]
            value = l.split(' ')[1]
            key_list.append(key)
            if i < args.number_pairs:
                if i == 0:
                    root = bt.Node(key, value)
                    i += 1
                else:
                    bt.insert(root, key, value)
                    i += 1
            else:
                break
        end = time.time()
        print('It requires %8.7f seconds to insert %s keys to the binary tree.' %((end - start), args.number_pairs))

        # searching existing keys
        start = time.time()
        for key in key_list:
            bt.search(root, key)
        end = time.time()
        print('It requires %8.7f seconds to search for all the %s keys inerted just now in the binary tree.' %((end - start), args.number_pairs))

        # searching non-existing keys
        start = time.time()
        for key in key_list:
            bt.search(root, key + '_non')
        end = time.time()
        print('It requires %8.7f seconds to search for %s non-existing keys in the binary tree.\n' %((end - start), args.number_pairs))



if __name__ == '__main__':
    main()
