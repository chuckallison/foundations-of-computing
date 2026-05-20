# Implements perorder and postorder per Figure 6–9
''' Output:
Preorder: + a * b ^ c ^ d + e f 
Postorder:  a b c d e f + ^ ^ * +
'''

class Node:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

def preorder(node):
    if node:
        return node.label + ' ' + preorder(node.left) + preorder(node.right)
    else:
        return ''

def postorder(node):
    if node:
        return postorder(node.left) + postorder(node.right) + ' ' + node.label
    else:
        return ''

expr = Node('+',
    Node('a'), Node('*',
        Node('b'), Node('^',
            Node('c'), Node('^',
                Node('d'), Node('+',
                    Node('e'), Node('f'))))))
print('Preorder:', preorder(expr))
print('Postorder:', postorder(expr))
