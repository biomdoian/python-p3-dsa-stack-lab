class Stack:

    def __init__(self, items=[], limit=100):
        """
        Initializes a new Stack instance.
        Uses a list as the underlying data structure.
        Can be initialized with a list of existing items.
        Takes an optional 'limit' to set the maximum size of the stack.
        """
        self.items = list(items)
        self._limit = limit

    def isEmpty(self):
        """
        Returns True if the Stack is empty; False otherwise.
        Time Complexity: O(1)
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Adds an element to the top of the stack.
        If the stack is full, it does nothing (to align with the provided test behavior).
        Time Complexity: O(1) (amortized, due to list append)
        """
        if self._limit is not None and len(self.items) >= self._limit:
            return
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the element from the top of the stack.
        Returns None if the stack is empty (stack underflow).
        Time Complexity: O(1)
        """
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        """
        Returns the value of the element at the top of the stack without removing it.
        Returns None if the stack is empty.
        Time Complexity: O(1)
        """
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        """
        Returns the number of elements contained in the Stack.
        Time Complexity: O(1)
        """
        return len(self.items)

    def full(self):
        """
        Returns True if the Stack is full; False otherwise.
        Only relevant if a limit is set.
        Time Complexity: O(1)
        """
        if self._limit is None:
            return False
        return len(self.items) >= self._limit

    def search(self, target):
        """
        Returns the distance between the top of the stack and the target element if it's present.
        If the target element is at the top of the stack, returns 0.
        Returns -1 if the target element is not present.
        Time Complexity: O(N) (due to list iteration/search)
        """
        try:
            
            index_from_bottom = self.items.index(target)
           
            distance = len(self.items) - 1 - index_from_bottom
            return distance
        except ValueError:
           
            return -1