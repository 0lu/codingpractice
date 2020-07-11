Time complexity:
O(N) - where N is total number of files in directory and sub directories

I used recursion here, the base case is when there is no folder in the 
current directory and if there is a folder in the current directory the 
recursive calls are made to check those subfolders. its synonymous
to traversing a binary tree. where files are the leaf nodes and directories
are parent nodes

Space complexity:
O(h) - where h is the size of the resultant array

Each recursive call is pushed to the stack and the maximum of the total number of recursive
calls at any point is the space complexity.