import time

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node
        if value < self.value:
            # if there is no self.left value
            if not self.left:
                # set the new left child to be new value
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # the new value is greater than the current node
        # go right
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the root node, is the target value, we found the value
        if self.value == target:
            return True    
        # target is smaller, go left
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

        # target is greater, go right
        else:
            if not self.right:
                return False
            else:
               return self.right.contains(target)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# # use a binary search tree with the first name

bst = BinarySearchTree(names_1[0])

# add the rest of the names with insert property
for i in range(1, len(names_1)):
    bst.insert(names_1[i])

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# loop over the second list of names using the contains property
# Searching through a binary search tree significantly decrease the time it takes to find matching names

for i in range(len(names_2)):
    if bst.contains(names_2[i]):
        duplicates.append(names_2[i])

#runtime: 0.12186408042907715 seconds


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

# used set from python just for fun and it was exponentailly faster: runtime: 0.12186408042907715 seconds
# duplicates = []

# setFirst = set(names_1)
# for name in names_2:
#     if name in setFirst:
#         duplicates.append(name)