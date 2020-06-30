Time complexity:
Union:
O(l1 + l2)
l1 = length of list 1
l2 = length of list 2

Intersection:
O(l1 + l2)
l1 = length of list 1
l2 = length of list 2

Since all elements in both lists are visited once, the time complexity
is the length of the sum of the elements in both lists 

Space complexity:
Union:
O(k)
k is the number of unique elements in both lists

Intersection:
O(l1)
l1 is the length of list1, although it can be optimized to be the 
min(l1, l2)
l1 = length of list 1
l2 = length of list 2

Since a set is used to keep track of seen items, the space complexity
is the total size required for the set in both cases


