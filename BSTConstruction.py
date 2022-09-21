class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    if len(preOrderTraversalValues)==0:
        return

    currentvalue=preOrderTraversalValues[0]
    rightidx=len(preOrderTraversalValues)

    for idx in range(1,len(preOrderTraversalValues)):
        value=preOrderTraversalValues[idx]
        if value>=currentvalue:
            rightidx=idx
            break

    lefttree=reconstructBst(preOrderTraversalValues[1:rightidx])
    righttree=reconstructBst(preOrderTraversalValues[rightidx:])
    return BST(currentvalue,lefttree,righttree)