To solve this problem, the idea is to use binary search. Instead of simply comparing the target to the middle point of the array, I should determine which part of the array is sorted. Say left is sorted. Then if key be searched lies in range of the left array, recur for the left array. Otherwise recur for the right array.


Time Complexity: O(log(n)) Space Complexity: O(1)