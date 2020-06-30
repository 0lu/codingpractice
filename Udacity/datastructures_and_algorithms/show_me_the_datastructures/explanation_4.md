Time complexity:
O(n) - where n is the number of users and groups in total considering users
in sub groups. They all form a tree the edges of the tree are users and
groups are parents

Space complexity:
O(k) - where k is the maximum depth of nesting of user and groups. Analogous
to the height of the tree

I used recursion, the base case is if there is no subgroup. If there is a 
sub group I called the function again to check the subgroups recursively