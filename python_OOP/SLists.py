# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""


class Node:
    """Create class Node."""

    def __init__(self, value):
        """Define class-level attributes of Node       ."""
        self.value = value
        self.next = None


class SList:
    """Create class SList."""

    def __init__(self, value):
        """Set        ."""
        self.head = Node(value)

    def add_node(self, value):
        """Add node (with value specified) to the end of the list."""
        runner = self.head
        while(runner.next):  # don't need to check for != None
            runner = runner.next
        runner.next = Node(value)
        return self

    def print_all_values(self, msg=""):
        """Print all values in the list."""
        runner = self.head
        print("\n\nhead points to ", id(self.head))
        print("Printing values in the list ---", msg, "---")
        while(runner.next):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))
        return self

    def remove_node(self, value):
        """Remove node with specified value."""
        runner = self.head
        if(runner.value == value):
            self.head = runner.next
            return self
        prev_runner = runner
        while(runner.next and runner.value != value):
            prev_runner = runner
            runner = runner.next
        if(runner.value == value):
            prev_runner.next = runner.next
        return self

    def insert_node(self, value, index):
        """Insert new node in list, with value and index as specified."""
        i = 0
        node = Node(value)
        runner = self.head
        if(i == index):
            node.next = self.head
            self.head = node
        while(runner):
            i += 1
            if(i == index):
                node.next = runner.next
                runner.next = node
            runner = runner.next
        return self


print("\n\n\n=========== START OF THE PROGRAM ===========")
sList = SList(5).add_node(7).add_node(9).add_node(1)
sList.printAllValues("Part 1")

sList.removeNode(12).removeNode(1)
sList.printAllValues("Part 2")

sList.insert_node(12, 3)
sList.printAllValues("Part 3")
