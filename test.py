from bintree import BinTree

def int_comp(curr, new):
    if curr > new:
        return 1
    elif curr < new:
        return -1
    else:
        return 0

b = BinTree(666);
print(b)

print(b.data)
print(b.left)
print(b.right)

b = b.insert(777, int_comp)
b = b.insert(888, int_comp)
b = b.insert(555, int_comp)

# b.left = BinTree(777)
# b.right = BinTree(888)

print(b.listify())
