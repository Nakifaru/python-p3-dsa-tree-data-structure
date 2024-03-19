child_three = {
    'value': 45,
    'left_child': None,
    'right_child': None
}


child_one = {
    'value': 50,
    'left_child': child_three,
    'right_child': None
}

child_two = {
    'value': 39,
    'left_child': None,
    'right_child': None
}

root_node = {
    'value': 20,
    'left_child': child_one,
    'right_child': child_two
}

class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None