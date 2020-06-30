Time complexity:
Encoding:
O(n) - count no of characters
O(knlogn) - heap operations in multiples of n times 
O(2n) - traverse tree to generate encoding 
O(n) - compose result

Overall = O(nlogn)

n = no of characters in string
k = an integer greater than 0

Decoding:
O(hn)
h = height of huffman tree
n = no of characters in string

Space complexity
Encoding:
O(k) - dictionary
O(2n) - heap
O(n) - recursion stack when generating encoding

Overall - O(n)
k = no of unique elements
n = no of characters in string

Decoding:
O(1) - constant space