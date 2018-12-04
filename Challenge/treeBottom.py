#You are given a recursive notation of a binary tree: each node of a tree is represented as a set of three elements:

#value of the node;
#left subtree;
#right subtree.
#So, a tree can be written as (value left_subtree right_subtree). It is guaranteed that 1 ≤ value ≤ 10**9. If a node doesn't exist then it is represented as an empty set: (). For example, here is a representation of a tree in the given picture:

#(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))

#Your task is to obtain a list of nodes, that are the most distant from the tree root, in the order from left to right.

#In the notation of a node its value and subtrees are separated by exactly one space character.

#Example

#For

#tree = "(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))"
#the output should be
#treeBottom(tree) = [5, 11, 4].

#Input/Output

#[execution time limit] 4 seconds (py)

#[input] string tree

#Guaranteed constraints:
#5 ≤ tree.length ≤ 120.

#[output] array.integer

#[Python2] Syntax Tips

def treeBottom(tree):
    x , y, k = 0, 0, len(tree)
    for j in range(1,k):
        if not tree[j].isdigit(): break
    for i in range(j+1,k):
        if tree[i] == "(": x += 1
        if tree[i] == ")": y += 1
        if x == y: break
    l, r = tree[j+1:i+1], tree[i+2:k-1]
    if l==r=="()": return [int(tree[1:j])]
    if depthMost(l) < depthMost(r): return treeBottom(r)
    if depthMost(l) > depthMost(r): return treeBottom(l)
    return treeBottom(l)+treeBottom(r)
        
def depthMost(tree):
    if tree == "()": return 0
    x , y, k = 0, 0, len(tree)
    for j in range(1,k):
        if not tree[j].isdigit(): break
    for i in range(j+1,k):
        if tree[i] == "(": x += 1
        if tree[i] == ")": y += 1
        if x == y: break
    l, r = tree[j+1:i+1], tree[i+2:k-1]
    return 1+max(depthMost(l),depthMost(r))


