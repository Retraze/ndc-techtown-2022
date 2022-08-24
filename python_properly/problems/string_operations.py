
# Your task is to implement these functions using builtins and slicing notation
# Do not use any imports

# run the tests as follows:
#   $ poetry run pytest tests/problems/test_string_operations.py -x -v


def get_string_length(string):
    return 0

# HINT: isinstance(x, bytes)
def convert_to_string(something):
    return something

def make_uppercase(string):
    return string

def make_lowercase(string):
    return string

def take_first_3_characters(string):
    return string

def take_every_other_character(string):
    return string

def take_last_8_characters(string):
    return string

# HINT: str.split
def count_words(string):
    return string

# HINT: str.join
def remove_first_word(string):
    return string

def censor_curse_words(string, list_of_bad_words):
    "this function replaces bad words with '***'"
    return string

# HINT: ord, hex
def convert_to_hexadecimal(string):
    return string

# HINT:
def convert_list_of_unicode_codepoints_to_string(list_of_codepoints):
    return list_of_codepoints

def convert_list_of_ints_to_bytes(list_of_uint8):
    return list_of_uint8

# HINT: str.endswith
def check_if_filename_has_filetype(filename: str, accepted_file_extensions: list) -> bool:
    return False
