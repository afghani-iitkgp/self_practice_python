
#                                                   MinHeap operations
# Insertion O(logn): Finding the exact position of the new element is performed in log nlogn since it is only compared with the position of the parent nodes.
# Delete Min O(logn): After the minimum element is removed, the heap has to put the new root in place.
# Find Min O(1): This is possible because the heap data structure always has the minimum element on the root node.
# Heapify O(n): This operation rearranges all the nodes after deletion or insertion operation. The cost of this operation is nn since all the elements have to be moved to keep the heap properties.
# Delete O(logn): A specific element from the heap can be removed in log nlogn time.

#                          5
#                       /      \      
#                      9        6
#                     / \      /  \
#                    11  10   13   7
                    


