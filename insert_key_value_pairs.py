import os
import sys
import time
import argparse
import binary_tree as bt
sys.path.insert(1, 'hash-tables-wehs7661')   # noqa: E402
sys.path.insert(2, 'avl_tree')               # noqa: E402
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
                        choices=['hash', 'AVL', 'tree'],
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
                        help='The number of data (key/value pairs) to be used.',
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

    if args.data_structure == 'hash':
        pass
    elif args.data_structure == 'AVL':
        pass
    elif args.data_structure == 'tree':
        # key insertion
        i = 0     # number of pairs taken in / line number
        start = time.time()
        for l in lines:
            key = l.split(' ')[0]
            value = l.split(' ')[1]
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
        print('The time for the key insertion by the binary tree is %s seconds.' % str(
            end - start))

        # key searching
        


if __name__ == '__main__':
    main()
