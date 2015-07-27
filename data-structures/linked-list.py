class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, new_value):
        self.value = new_value

    def set_next(self, new_next):
        self.next = new_next

    def reveal(self):
        print('Value: %s' % self.value)
        print('Next: %s' % self.next)


class Linked_List(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

        if self.tail == None:
            self.tail = new_node

    def add_to_tail(self, value):
        if self.head == None:
            add_to_head(value)
        else:
            new_node = Node(value)
            self.tail.set_next(new_node)
            self.tail = new_node

    def size(self):
        current_node = self.head
        count = 0
        while current_node != None:
            count += 1
            current_node = current_node.get_next()

        return count

    def contains(self, value):
        current_node = self.head
        found = False
        while current_node != None and not found:
            if current_node.get_value() == value:
                found = True
            else:
                current_node = current_node.get_next()

        return found

    def remove(self, value):
        current_node = self.head
        previous_node = None
        found = False
        while not found:
            if current_node.get_value() == value:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        if previous_node == None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())

    def print_out(self):
        current_node = self.head
        while current_node != None:
            print(current_node.get_value())
            # print('\n')
            current_node = current_node.get_next()




    def is_empty(self):
        return self.head == None

linked_list = Linked_List()

linked_list.add_to_head('c')
linked_list.add_to_head('c')
linked_list.add_to_head('b')
linked_list.add_to_head('a')
linked_list.add_to_tail('d')
linked_list.add_to_tail('e')


print(linked_list.contains('a')) # --> True
print(linked_list.contains('f')) # --> False
linked_list.print_out()



