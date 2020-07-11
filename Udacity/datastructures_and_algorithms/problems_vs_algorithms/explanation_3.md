Design Choice and DS Algo used With Brief Explanation:
- I used a max heap to store the elements and used a greedy approach to pick
the largest element each time and add to the numbers.

Big(O) Time with a brief explanation, mention what is N
Time complexity:
O(n) - heapify
O(nlogn) - pop all from heap
Overall - O(nlogn)
n - length of the array

Big(O) Space with a brief explanation, mention what is N and Call stack for recursive solutions
- O(1) constant space complexity, heapified the existing array