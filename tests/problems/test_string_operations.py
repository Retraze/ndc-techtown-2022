import techtown2022.problems.string_operations as problems
import pytest

# you can run these tests like so:
#   $ poetry run pytest tests/problems/test_string_operations.py -x -v



def test_get_string_length():
    assert problems.get_string_length("a")    == 1
    assert problems.get_string_length("aa")   == 2
    assert problems.get_string_length("aaa")  == 3
    assert problems.get_string_length("aaaa") == 4

def test_convert_to_string():
    assert problems.convert_to_string(5)    == "5"
    assert problems.convert_to_string(5.5)  == "5.5"
    assert problems.convert_to_string(b"5") == "5"

def test_make_uppercase():
    assert problems.make_uppercase("FooBar") == "FOOBAR"
    assert problems.make_uppercase("foobar") == "FOOBAR"
    assert problems.make_uppercase("FOOBAR") == "FOOBAR"
    assert problems.make_uppercase("fOOBAR") == "FOOBAR"


def test_make_lowercase():
    assert problems.make_lowercase("FooBar") == "foobar"
    assert problems.make_lowercase("foobar") == "foobar"
    assert problems.make_lowercase("FOOBAR") == "foobar"
    assert problems.make_lowercase("fOOBAR") == "foobar"


def test_take_first_3_characters():
    assert problems.take_first_3_characters("12345789") == "123"
    assert problems.take_first_3_characters("qwetuibb") == "qwe"
    assert problems.take_first_3_characters("foobar")   == "foo"


def test_take_every_other_character():
    assert problems.take_every_other_character("12345789") == "1358"
    assert problems.take_every_other_character("qwetuibb") == "qeub"
    assert problems.take_every_other_character("foobar")   == "foa"


def test_take_last_8_characters():
    assert problems.take_last_8_characters("This is a sentence that may have bad words in it.")     == "s in it."
    assert problems.take_last_8_characters("It is therefore important that we censor it properly!") == "roperly!"


def test_count_words():
    assert problems.count_words("This is a sentence that may have bad words in it.")     == 11
    assert problems.count_words("It is therefore important that we censor it properly!") == 9


def test_remove_first_word():
    assert problems.remove_first_word("This is a sentence that may have bad words in it.")     == "is a sentence that may have bad words in it."
    assert problems.remove_first_word("It is therefore important that we censor it properly!") == "is therefore important that we censor it properly!"


def test_censor_curse_words():
    bad_words = ["sentence", "That", "ords", "it"]
    assert problems.censor_curse_words("This is a sentence that may have bad words in it.",     bad_words) == "This is a *** *** may have bad words in it."
    assert problems.censor_curse_words("It is therefore important that we censor it properly!", bad_words) == "*** is therefore important *** we censor *** properly!"


def test_convert_to_hexadecimal():
    assert problems.convert_to_hexadecimal("foobar") == "66 6f 6f 62 61 72"
    assert problems.convert_to_hexadecimal("query")  == "71 75 65 72 79"


def test_convert_list_of_unicode_codepoints_to_string():
    data = [104, 101, 108, 108, 111, 32, 116, 104, 101, 114, 101]
    assert problems.convert_list_of_unicode_codepoints_to_string(data) == "hello there"
    data = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
    assert problems.convert_list_of_unicode_codepoints_to_string(data) == "Hello, World!"
    data = [128526]
    assert problems.convert_list_of_unicode_codepoints_to_string(data) == "😎"

def test_convert_list_of_ints_to_bytes():
    data = [104, 101, 108, 108, 111, 32, 116, 104, 101, 114, 101]
    assert problems.convert_list_of_ints_to_bytes(data) == b"hello there"
    data = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
    assert problems.convert_list_of_ints_to_bytes(data) == b"Hello, World!"
    data = [128526]
    with pytest.raises(ValueError):
        problems.convert_list_of_ints_to_bytes(data) == "Hello, World!"

def test_check_if_filename_has_filetype():
    assert problems.check_if_filename_has_filetype("foobar.txt",  ["txt", "md", "png"])
    assert problems.check_if_filename_has_filetype("foobar.md",   ["txt", "md", "png"])
    assert problems.check_if_filename_has_filetype("foobar.png",  ["txt", "md", "png"])
    assert not problems.check_if_filename_has_filetype("foobar_txt",  ["txt", "md", "png"]), "the dot is not checked"
    assert not problems.check_if_filename_has_filetype("foobar_md",   ["txt", "md", "png"]), "the dot is not checked"
    assert not problems.check_if_filename_has_filetype("foobar_png",  ["txt", "md", "png"]), "the dot is not checked"
    assert problems.check_if_filename_has_filetype("foobar.JPEG", ["jpeg"]), "have you handled casing?"
    assert problems.check_if_filename_has_filetype("foobar.jpeg", ["JPEG"]), "have you handled casing?"
