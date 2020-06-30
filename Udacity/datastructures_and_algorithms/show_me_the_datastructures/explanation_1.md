Time complexity:
get - 0(1)
set - 0(1)

Space complexity:
O(1) - no extra space is assigned

I used a hashtable to locate elements in O(1) and a doubly linked list to 
keep the usage. Whenever an item is accessed it is placed at the head of the 
list. when the cache is full the last item in the linked list is removed
to make room for the new item that is added to the head of the linked list