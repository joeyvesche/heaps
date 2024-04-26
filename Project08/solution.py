"""
Ian Barber, Alex Woodring, Max Huang, and Angelo Savich
Project 8 - Heaps - Solution Code
CSE 331 Spring 2022

"""
from typing import List, Tuple, Any


class MinHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = []

    def __str__(self) -> str:
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data)

    __repr__ = __str__

    def to_tree_format_string(self) -> str:
        """
        Prints heap in Breadth First Ordering Format
        :return: String to print
        """
        string = ""
        # level spacing - init
        nodes_on_level = 0
        level_limit = 1
        spaces = 10 * int(1 + len(self))

        for i in range(len(self)):
            space = spaces // level_limit
            # determine spacing

            # add node to str and add spacing
            string += str(self.data[i]).center(space, ' ')

            # check if moving to next level
            nodes_on_level += 1
            if nodes_on_level == level_limit:
                string += '\n'
                level_limit *= 2
                nodes_on_level = 0
            i += 1

        return string

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def __len__(self) -> int:
        """
            Returns the length of the heap
            :return: length of the heap
        """
        return len(self.data)

    def empty(self) -> bool:
        """
            Checks if the heap is empty
            :return: True if empty
        """
        return len(self) == 0

    def top(self) -> int:
        """
            Returns the top value of the MinHeap
            :return: Top value of MinHeap
        """
        if self.empty():
            return None
        return self.data[0]

    def get_left_child_index(self, index: int) -> int:
        """
            Computes the index of the left child at the parent
            :param index: Parent index position
            :return: Index of the left child
        """
        if ((2 * index) + 1) >= len(self.data):
            return None
        return (2 * index) + 1

    def get_right_child_index(self, index: int) -> int:
        """
            Computes the index of the right child at the parent index
            :param index: Parent index position
            :return: Index of the right child
        """
        if ((2 * index) + 2) >= len(self.data):
            return None
        return (2 * index) + 2

    def get_parent_index(self, index) -> int:
        """
            Computes the index of the parent at the child index
            :param index: Child index position
            :return: Index of parent
        """
        if (index - 1) // 2 < 0:
            return None
        return (index - 1) // 2

    def get_min_child_index(self, index: int) -> int:
        """
            Computes the index of the child with the lower value at the parent
            :param index: Parent index position
            :return: The minimum value child's index
        """
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)

        if left is not None and right is not None:
            if self.data[left] < self.data[right]:
                return left

            else:
                return right

        elif left is None and right is None:
            return None

        else:
            return left

    def percolate_up(self, index: int) -> None:
        """
            Percolates up the value at index
            :param index: Index to start at
            :return: None
        """
        parent = self.get_parent_index(index)
        if index > 0 and self.data[index] < self.data[parent]:
            self.data[index], self.data[parent] = self.data[parent], self.data[index]
            self.percolate_up(parent)

    def percolate_down(self, index: int) -> None:
        """
            Percolates down the value at index
            :param index: Index to start at
            :return: None
        """
        if self.get_left_child_index(index) is not None:
            left = self.get_left_child_index(index)
            small_child = left
            if self.get_right_child_index(index) is not None:
                right = self.get_right_child_index(index)
                if self.data[right] < self.data[left]:
                    small_child = right
            if self.data[small_child] < self.data[index]:
                self.data[index], self.data[small_child] = self.data[small_child], self.data[index]
                self.percolate_down(small_child)

    def push(self, val: int) -> None:
        """
            Pushes the value to the heap
            :param val: Value to push onto the heap
            :return: None
        """
        self.data.append(val)
        self.percolate_up(len(self.data) - 1)

    def pop(self) -> int:
        """
            Removes the top element from the heap
            :return: The value that was popped
        """
        if self.empty():
            return None

        self.data[0], self.data[len(self.data) - 1] = self.data[len(self.data) - 1], self.data[0]
        item = self.data.pop()
        self.percolate_down(0)
        return item


class MaxHeap:
    """
    Partially completed data structure. Do not modify completed portions in any way
    """
    __slots__ = ['data']

    def __init__(self):
        """
        Initializes the priority heap
        """
        self.data = MinHeap()

    def __str__(self):
        """
        Converts the priority heap to a string
        :return: string representation of the heap
        """
        return ', '.join(str(item) for item in self.data.data)

    __repr__ = __str__

    def __len__(self):
        """
        Length override function
        :return: Length of the data inside the heap
        """
        return len(self.data)

    def print_tree_format(self):
        """
        Prints heap in bfs format
        """
        self.data.to_tree_format_string()

    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   Modify below this line

    def empty(self) -> bool:
        """
            Checks if the heap is empty
            :return: True if empty
        """
        return self.data.empty()

    def top(self) -> int:
        """
            Returns the top value of the MaxHeap
            :return: Top value of MaxHeap
        """
        num = self.data.top()
        if num is None:
            return None
        return num * -1

    def push(self, key: int) -> None:
        """
            Pushes the value to the heap
            :param key: Value to push onto the heap
            :return: None
        """
        self.data.push(key * -1)

    def pop(self) -> int:
        """
            Removes the top element from the heap
            :return: The value that was popped
        """
        return self.data.pop() * -1


def current_medians(values) -> List[int]:
    """
         find the median value after each value is added to the median computation
         :param values: A list of integer values, in the order to be added into the median calculation
         :return: A list of medians in the order they were computed
    """

    min = MinHeap()
    max = MaxHeap()
    median = []

    for i in values:
        if not min and not max:
            median.append(i)
            max.push(i)

        elif max:
            if i >= max.top():
                min.push(i)

            else:
                max.push(i)

            if len(max) == len(min):
                median.append((max.top() + min.top()) / 2)

            elif len(max) == len(min) + 1:
                median.append(max.top())

            elif len(min) == len(max) + 1:
                median.append(min.top())

            elif len(min) == len(max) + 2:
                max.push(min.pop())
                median.append((min.top() + max.top()) / 2)

            elif len(max) == len(min) + 2:
                min.push(max.pop())
                median.append((max.top() + min.top()) / 2)

    return median






