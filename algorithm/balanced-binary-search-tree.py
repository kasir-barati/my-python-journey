from typing import List

# https: // www.youtube.com/watch?v = iiaxxJdqLTM


class BinaryTree:
    value = None
    left = None
    right = None

    def __init__(self, value=None) -> None:
        self.value = value

    def ordered_list(self) -> List[int]:
        left_side = [] if self.left == None else self.left.ordered_list()
        middle_side = [] if self.value == None else [self.value]
        right_side = [] if self.left == None else self.right.ordered_list()

        return left_side + middle_side + right_side


tree = BinaryTree()
tree.add
