
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value



def dfs_preorder(node):
    if node:
        print(node.value, end=" ")
        dfs_preorder(node.left)
        dfs_preorder(node.right)


def dfs_inorder(node):
    if node:
        dfs_inorder(node.left)
        print(node.value, end=" ")
        dfs_inorder(node.right)


def dfs_postorder(node):
    if node:
        dfs_postorder(node.left)
        dfs_postorder(node.right)
        print(node.value, end=" ")

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)


n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n5.left = n6
n5.right = n7
n3.left = n8
n3.right = n9
n9.left = n10

print("Pre-Order")
dfs_preorder(n1)
print("\n")

print("In-Order")
dfs_inorder(n1)
print("\n")


print("Post-Order")
dfs_postorder(n1)
print("\n")
