import python_properly.problems.packing as problems
import pytest
import functools

# you can run these tests like so:
#   $ poetry run pytest tests/problems/test_packing.py -x -v

class NoConcat(list):
    def __add__(self, other):
        return NotImplemented

class NoGetItem(list):
    def __getitem__(self, index):
        raise KeyError("Try not to use list indexing, use unpacking instead ;)")


def test_remove_first_and_last_items_using_unpacking():
    assert problems.remove_first_and_last_items_using_unpacking([1, 2, 3, 4]) == [2, 3]
    assert problems.remove_first_and_last_items_using_unpacking([1, 2, 3])    == [2]
    assert problems.remove_first_and_last_items_using_unpacking([1, 2])       == []
    with pytest.raises(ValueError):
        problems.remove_first_and_last_items_using_unpacking([1])
    with pytest.raises(ValueError):
        problems.remove_first_and_last_items_using_unpacking([])

def test_swap_the_third_and_firth_item_using_packing_and_unpacking():

    assert list(problems.swap_the_third_and_fifth_item([1, 2, 3, 4, 5]))          == [1, 2, 5, 4, 3]
    assert list(problems.swap_the_third_and_fifth_item([1, 2, 3, 4, 5, 6, 7, 8])) == [1, 2, 5, 4, 3, 6, 7, 8]

def test_join_two_lists_using_packing():
    list1 = ["foo", "bar"]
    list2 = [1, 2, 3]
    list3 = range(3)
    list1_nc = NoConcat(list1)
    list2_nc = NoConcat(list2)
    list3_nc = NoConcat(list3)

    assert problems.join_two_lists_using_packing(list1,    list1)    == ["foo", "bar", "foo", "bar"]
    assert problems.join_two_lists_using_packing(list1,    list2)    == ["foo", "bar", 1, 2, 3]
    #assert problems.join_two_lists_using_packing(list1,    list3)    == ["foo", "bar", 0, 1, 2]
    assert problems.join_two_lists_using_packing(list1_nc, list1_nc) == ["foo", "bar", "foo", "bar"]
    assert problems.join_two_lists_using_packing(list1_nc, list2_nc) == ["foo", "bar", 1, 2, 3]
    assert problems.join_two_lists_using_packing(list1_nc, list3_nc) == ["foo", "bar", 0, 1, 2]

def test_double_first_and_halve_second():
    data = [
        (1, 2),
        (2, 4),
        (3, 6),
        (4, 8),
        ("foo", 10),
        ("bar", 12),
    ]
    target = [
        (2, 1),
        (4, 2),
        (6, 3),
        (8, 4),
        ("foofoo", 5),
        ("barbar", 6),
    ]
    assert problems.double_first_and_halve_second(data) == target

def test_unpack_the_third_item_in_the_second_item():
    assert problems.unpack_the_third_item_in_the_second_item([1, [2, 3, 4]])       == 4
    assert problems.unpack_the_third_item_in_the_second_item([1, [2, 3, 4], 5])    == 4
    assert problems.unpack_the_third_item_in_the_second_item([1, [2, 3, 4, 5], 6]) == 4
    assert problems.unpack_the_third_item_in_the_second_item([1, NoGetItem([2, 3, 4, 5]), 6]) == 4
    assert problems.unpack_the_third_item_in_the_second_item([NoGetItem(range(x,   x+7))  for x in NoGetItem(range( 6, 10))]) == 9
    assert problems.unpack_the_third_item_in_the_second_item([NoGetItem(range(x+3, x+20)) for x in NoGetItem(range(12, 40))]) == 18

def test_make_list_from_generator_using_unpacking(mocker):
    assert problems.make_list_from_generator_using_unpacking([1, 2, 3]) == [1, 2, 3]
    assert problems.make_list_from_generator_using_unpacking(range(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert problems.make_list_from_generator_using_unpacking((i for i in range(4))) == [0, 1, 2, 3]
