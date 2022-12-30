"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position < 1:  # Just in case the position is too small
            return
        current = self.head
        while current and position > 1:
            position -= 1
            current = current.next
        return current
        
  
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        new_node = new_element
        if position < 1:
            print("Error")
        else:
            current = self.head
            counter = 0
            while current:
                counter += 1
                if counter == position -1:
                    temp = current.next
                    current.next = new_node
                    new_node.next = temp
                    break
                else:
                    current = current.next

    def display(self):
        current = self.head
        while(current.next != None):
            print(current.value)
            current = current.next
        print(current.value)
                
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.next:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                break
            else:
                previous = current
                current = current.next



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print (ll.head.next.next.value)
# Should also print 3
print (ll.get_position(3).value)

# Test insert
print("display")
ll.display()
print("before insert")
ll.insert(e4,3)
print("after insert")
ll.display()
# Should print 4 now
print (ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print (ll.get_position(1).value)
# Should print 4 now
print (ll.get_position(2).value)
# Should print 3 now
print (ll.get_position(3).value)