The idea to solve this problem is to use binary search. If mid * mid < target, do binary search between mid + 1 and target. In this case, I also update the result because we need floor. If mid * mid > target, do binary search between start and mid.

Time Complexity: O(log(n)) Space Complexity: O(1)