
# Your task is to implement these functions using list comprehensions, slicing syntax, and builtin functions only.
# Do not use any imports

# run the tests as follows:
#   $ poetry run pytest tests/list_comprehensions/test_problems.py -x -vv

# The tests uses external or weird solutions to achieve the same thing


DATA = [
    2, 4, 5, 6, 3,
    7, 3, 5, 5, 87,
    8, 3, 3, 3, 5,
    7, 7, 2, 4, 7,
    9, 8, 5, 3, 2,
]

NESTED_DATA = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8],
    [9],
]

MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]


def compute_average(data):
    # Add all items together, then divide the result by the number of elements
    pass

def compute_variance(data):
    # Subtract the avarage from each item, raise them to the power of 2, then add them all together, then divide by number of elements
    pass

def largest_element(data):
    # Return the largest item in data
    pass

def smallest_element(data):
    # Return the smallest item in data
    pass

def every_third(data):
    # Return every third item in data
    pass

def even_only(data):
    # Return only the even elements (x % 2 == 0)
    pass

def take_first_5(data):
    # Return only the even elements (x % 2 == 0)
    pass

def reversed(data):
    # Return the data in reverse order
    pass

def flatten(nested_data):
    # Flatten a nested list into a normal list.
    # [[1, 2], [3, 4]] -> [1, 2, 3, 4]
    pass

def transpose(matrix):
    # Flip/mirror the matrix abouts its diagonal (the line from [0][0] to [-1][-1])
    # HINT: zip
    # HINT: unpacking
    pass


# You can run this module as follow:
#   $ poetry run python -m python_proficiency.list_comprehensions.problems

if __name__ == "__main__":
    from rich import print
    print(f"{DATA                    = }")
    print(f"{compute_average(DATA)   = }")
    print(f"{compute_variance(DATA)  = }")
    print(f"{largest_element(DATA)   = }")
    print(f"{smallest_element(DATA)  = }")
    print(f"{every_third(DATA)       = }")
    print(f"{even_only(DATA)         = }")
    print(f"{take_first_5(DATA)      = }")
    print(f"{reversed(DATA)          = }")
    print(f"{NESTED_DATA             = }")
    print(f"{flatten(NESTED_DATA)    = }")
    print(f"{MATRIX                  = }")
    print(f"{transpose(MATRIX)       = }")
