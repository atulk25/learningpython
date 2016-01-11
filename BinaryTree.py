#
# Consider the binary tree shown below :
#
#      A
#    /   \
#   /     \
#   B      C
# /  \    / \
# D    G  E   H
#       /
#      F
# This tree can be represented as a sequence of (parent,child) tuples in some random order. For example :
# (B,D), (A,B), (C,E), (A,C), (E,F), (B,G), (C,H)
#
#
# In order to remove ambiguity in the above representation, we can assume that :
# 1) The (parent,left child) is always listed before (parent,right child). In the above example, B is the left child and
#    C is the right child of A, since A,B shows up before A,C
# 2) A node cannot have a right child without having a left child. So, if only 1 child is present, it is the left child.
#    In the above example, F is the left child of E.
# The same tree can be printed as follows :
# - A
#    -B
#        -D
#        -G
#    -C
#        -E
#            -F
#        -H
#
# Here, we are using indentation to denote children and print out the left child followed by the right child.
#
# Write a program to translate the first representation into the second.
#

import sys


class Node(object):
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def add(self, child):
        if self.left == None:
            self.left = child
        else:
            self.right = child

    def __repr__(self):
        return "({0}, {1}, {2})".format(self.label, self.left, self.right)

    def visit_preorder(self, level=0):
        print("\t" * level, self.label)

        if self.left is not None:
            self.left.visit_preorder(level + 1)

        if self.right is not None:
            self.right.visit_preorder(level + 1)


nodes = dict()
all_nodes = set()
child_nodes = set()


def get_node(label):
    nodes[label] = nodes.get(label, Node(label))
    return nodes[label]


def parse_input_file(file):
    return [tuple(line.strip().split(",")) for line in file]


if __name__ == "__main__":
    with open(sys.argv[1], "r") as input_file:
        nodes_list = parse_input_file(input_file)
        for parent, child in nodes_list:
            parent_node = get_node(parent)
            child_node = get_node(child)
            parent_node.add(child_node)
            all_nodes.add(parent)
            all_nodes.add(child)
            child_nodes.add(child)

    print(all_nodes)
    print(child_nodes)
    print("Root :", all_nodes - child_nodes)
    print(nodes)

    nodes[(all_nodes - child_nodes).pop()].visit_preorder()
