# create node class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


# create the queue class
class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("The following order has been added to the queue:" + "\n" + str(item_to_add.get_value()))
            print()
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, the queue is full")
            print()

    def dequeue(self):
        if self.get_size() > 0:
            item_to_remove = self.head
            print("The following order is being processed and has been deleted from the queue:"
                  + "\n" + str(item_to_remove.get_value()))
            print()

            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("There are no orders in the queue")
            print()


    def peek(self):
        if self.is_empty():
            print("There are no orders in the queue")
            print()
        else:
            print("The next order is: " + "\n" + self.head.get_value())
            print()

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0

# choose limit for queue
def choose_limit():
    limit_input = input("Please choose maximum number of orders you wish to hold in the queue (eg. 10, 15, 20): ")
    if limit_input.isnumeric():
        print()
        global list_of_orders
        list_of_orders = Queue(int(limit_input))
    else:
        print("Sorry, input not recognised")
        print()
        choose_limit()
choose_limit()

# add item to queue
def input_a_new_order():
    person = input("please input the person's name: ")
    item_ordered = input("Please input the item ordered: ")
    address = input("Please input their address: ")
    print()
    list_of_orders.enqueue(person + "\n" + item_ordered + "\n" + address)


# check the first item in the queue
def check_the_next_order():
    list_of_orders.peek()

# remove an item from the list
def process_an_order():
    list_of_orders.dequeue()

running = True
while running:
    print(" # Queue information # ")
    print("Current number of orders in queue: " + str(list_of_orders.size))
    print("Current number of spaces in queue: " + str(list_of_orders.max_size - list_of_orders.size))
    print("""
 # Options #
Add a new order to the queue (a)
View the next order to be processed (v)
Process the next order (and delete it from the queue) (p)""")
    input_choice = input("Please type a letter a press enter: ")
    if input_choice.strip().lower() == "a":
        print()
        input_a_new_order()
    if input_choice.strip().lower() == "v":
        print()
        check_the_next_order()
    if input_choice.strip().lower() == "p":
        print()
        process_an_order()

