'''
Created on Dec 5, 2018

@author: Jim
'''
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


