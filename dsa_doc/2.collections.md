# Collections
## List
It is a gorup of things and they have a specific order.
The order doesn't mean much, and I can add, remove elements in anypoint. Be aware that different programming languages implement them differently.
### Arrays
They are list-based collections. An array is a list with few added rules. In some languages you can have objects of the same type and in other you have elements of different type. In some languages the size is fixed and in others is not.
Each array has a location called index. Normally the index starts from 0. <br/> 
Highlights<br/>
- If you need to access a certain location in the middle the array is a good choice and you only need to keep track of the length. 
- Insertion and deletion can be more painful. Usually insertion at the end is ok, but it can be hard if it is full. If you have to insert in the middle or delete, then you have to shift the other elements and this can produce a linea complexity.
## Python Lists
Run time of Python collections https://wiki.python.org/moin/TimeComplexity <br/>
Python List fresh up: https://developers.google.com/edu/python/lists

## Linked Lists
A linked list is an extension of a list but it is not an array. A linked list is characteristed by links, each element has some notion of what the element list since it is connected into it but doesn't know about how long the list is or where it is in the list. 
In an array there is the information only because of the indexes, but elements don't know about other elements.

### Linked Lists in Depth
In high level programming languages usually there are only lists that combines the properties of arrays or linked lists.
In both cases we store the value and another element. For the array the other element is the index. For the linked list the element is "next" a reference to the next element of the linked list. This means assigning the actual next element as a property of the previous element. The element has a spaced dedicated to the memory location.<br/>
![Linked Lists Image](/dsa_doc/imgs/linked_lists.png "Linked Lists")<br/>
Inserting and deleting elements is easier. To add an element you only need to change the "next" reference to point to the new object. Be careful to not lose reference to other elements. The complexity is O(1) because we are just shifting pointers and not iterating over objects.

## Doubly Linked List
you can reverse the list in both directions. There is also an additional element called "prev" that points at the previous cell.
## Stacks
## Queue