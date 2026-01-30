⏱️ Time Complexity
O(max(n, m))
n = number of nodes in linked list l1
m = number of nodes in linked list l2

💾 Space Complexity
O(max(n, m))
✅ Why?
A new linked list is created to store the result
In the worst case, the result has:
max(n, m) nodes
+1 node if there is a final carry (e.g., 999 + 1 = 1000)
Only constant extra variables (carry, pointers) are used
📌 Input lists are not modified
