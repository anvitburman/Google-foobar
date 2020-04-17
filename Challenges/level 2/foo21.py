# Ion Flux Relabelling
# ======================
# This one is pretty annoying to explain without technical talks about trees so here, take this from the original probmlem question I looked up online because I saved none of them!

#    7
#  3   6
# 1 2 4 5

# Write a function answer(h, q) - where h is the height of the perfect tree of
# converters and q is a list of positive integers representing different flux
# converters - which returns a list of integers p where each element in p is the
# label of the converter that sits on top of the respective converter in q, or -1
# if there is no such converter.  For example, answer(3, [1, 4, 7]) would return
# the converters above the converters at indexes 1, 4, and 7 in a perfect binary
# tree of height 3, which is [3, 6, -1].
# Now that the problem make(at least some) sense I can say that this problem wasn’t much harder than the last one but used some basics of CS theory, trees in that case, but could totally be solved without its knowledge. In this case we get the biggest element that can find a top(ie top-1) and if our number is between this and 0 it will have a number above it. We then do a recursive check; if the item is equal or inferior to the top of the left node then it is in the left node, otherwise proceed with the right with the same logic until we find the number as either the left node or right node, making it on top of those.

def findX(item,cur,dif):
    right_node=cur-1
    left_node=right_node-dif//2

    if(right_node==item or left_node==item):
        return cur 
    else:
        if(item<=left_node):
            return findX(item,left_node,dif//2)
        else:
            return findX(item,right_node,dif//2)

def Solution(h, q):
    if(h > 30 or h < 1):
        raise ValueError('Height outside of bounds')
    if(len(q) > 10000 or len(q) < 1):
        raise ValueError('Flux converters list  outside of bounds')

    items=(2**h)-1

    arr=[]
    for i in range(len(q)):
        if (q[i]<items and q[i]>0):
            arr.append(findX(q[i],items,items-1))
        else:
            arr.append(-1)
    return arr