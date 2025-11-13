# Reverse a Linked List

prev is None because at the start, nothing comes before the first node in the list.

curr (the current node to be iterated on) is equal to the head which is the first node in the list.

```
prev = None
curr = head
```

As long as the current node to be iterated on is still inside the linked list, keep on running the code in the loop.

`while curr is not None:`

curr.next points to the node in the list that comes after the current node.

It is saved in a variable next_node so that the rest of the list is not lost.

`next_node = curr.next`

As we know, curr.next normally points forward (to the node that comes after).

Now we switch the arrow backwards (make curr.next point to the previous node, known as prev).

`curr.next = prev`

To move through with the rest of the list, we push the prev and current node pointers forward.

```
prev = curr
curr = next_node
```

Finally, we return prev which now points to the new head of the reversed list.

`return prev`
