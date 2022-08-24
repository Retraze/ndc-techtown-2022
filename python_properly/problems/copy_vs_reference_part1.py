# Your task is to implement the marked functions using only the provided modules, if any

# run the tests as follows:
#   $ poetry run pytest tests/problems/test_copy_vs_reference_part1.py -x -v

class User:
    def __init__(self, name, username, roles):
        self.name     = name
        self.username = username
        self.roles    = roles

    def add_role(self, role):
        self.roles.append(role)

    # TASK: make a copy of the user, that is separate from the original
    def duplicate(self):
        return self
