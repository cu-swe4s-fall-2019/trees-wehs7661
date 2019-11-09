#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle binary_tree.py
assert_no_stdout
run test_style pycodestyle avl.py
assert_no_stdout
run test_style pycodestyle gen_data.py
assert_no_stdout
run test_style pycodestyle test_trees.py
assert_no_stdout
run test_style pycodestyle insert_key_value_pairs.py

run bad_structure python insert_key_value_pairs.py -d AAA -i rand.txt -n 10000
assert_stderr
assert_in_stderr "invalid choice"

run bad_dataset python insert_key_value_pairs.py -d tree -i AAA.txt -n 10000
assert_stderr
assert_in_stderr "invalid choice"

run bad_number python insert_key_value_pairs.py -d tree -i rand.txt -n 20000
assert_stdout
assert_exit_code 1

run test_tree python insert_key_value_pairs.py -d tree -i rand.txt -n 1000
assert_stdout
assert_in_stdout "Results of the binary tree"
assert_exit_code 0

run test_tree python insert_key_value_pairs.py -d all -i rand.txt -n 1000
assert_stdout
assert_in_stdout "Results of the hash table"
assert_in_stdout "Results of the AVL tree"
assert_in_stdout "Results of the binary tree"
assert_exit_code 0

run test_gen_data python gen_data.py
assert_no_stdout 