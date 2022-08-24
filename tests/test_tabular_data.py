from python_properly import tabular_data
from python_properly.tabular_data import data
import pytest
import tabulate
import random
import functools
from pprint import pprint

# you can run these tests like this:
#   $ poetry run pytest tests/test_tabular_data.py -x 

def test_determine_n_columns():
    for _ in range(10):
        data = [
            [0] * random.randrange(5, 10)
            for _ in range(40)
        ]
        # this is a bad, solution, copying it isn't worth it ;)
        target = functools.reduce(lambda a, b: a if a > b else b, map(len, data), 0)

        assert tabular_data.determine_n_columns(data) == target

@pytest.mark.parametrize("targets", [[5, 7, 2], [9, 6, 2], [5, 5, 5], []])
def test_determine_column_widths(targets):
    data1 = [["#" * i for i in targets]] * 5
    data2 = [["#" * i for i in targets]] + [[]] * 4
    data3 = [[]] * 4 + [["#" * i for i in targets]]
    for data in [data1, data2, data3]:
        print("testing the following table:")
        pprint(data)
        assert tabular_data.determine_column_widths(data) == targets
        print()


ALIGN_ROW_TEST_DATA = [
    ([5, "##", 4.3], [6, 2, 9], "|", f"{5:>6}|{'##':<2}|{4.3:>9}"),
    ([5, "##", 4.3], [7, 5, 4], "#", f"{5:>7}#{'##':<5}#{4.3:>4}"),
]

@pytest.mark.parametrize("row,cell_sizes,sep,target", ALIGN_ROW_TEST_DATA)
def test_format_row(row, cell_sizes, sep, target):
    assert tabular_data.format_row(row, cell_sizes, sep) == target


@pytest.mark.parametrize("data,add_header", [(data.generate_people(6, add_header=add_header), add_header) for _ in range(20) for add_header in [True, False]])
def test_format_table(data, add_header):
    # map to str, since tabulate doesn't do alignment correctly...
    data = [[*map(str, row)] for row in data]

    target = tabulate.tabulate(
        # "tabulate" headers has forced minimum padding
        tabular_data.add_header_separator(data) if add_header else data,
        tablefmt = tabulate.TableFormat(
            lineabove        = None,
            linebelowheader  = None,
            linebetweenrows  = None,
            linebelow        = None,
            headerrow        = tabulate.DataRow("| ", " | ", " |"),
            datarow          = tabulate.DataRow("| ", " | ", " |"),
            padding          = 0,
            with_header_hide = None,
        ),
        numalign="right", # broken?
    )

    output = tabular_data.format_table(data, has_header=add_header)

    print("Target:")
    print(target)
    print()
    print("Output:")
    print(output)

    assert output == target


def test_reverse_table():
    data = [
        ["a", "b", "c"], # header
        ["1", "2", "3", "a"],
        ["1", "2", "3", "b"],
        ["1", "2", "3", "c"],
    ]
    target_1 = [ # preserving header
        ["a", "b", "c"],
        ["1", "2", "3", "c"],
        ["1", "2", "3", "b"],
        ["1", "2", "3", "a"],
    ]
    target_2 = [ # not preserving header
        ["1", "2", "3", "c"],
        ["1", "2", "3", "b"],
        ["1", "2", "3", "a"],
        ["a", "b", "c"],
    ]
    assert target_1 == tabular_data.reverse_table(data, has_header=True)
    assert target_2 == tabular_data.reverse_table(data, has_header=False)




def test_format_table_align():
    data = [
        ["##", "5", 5, "5.5", 5.5],
        ["##", 5, "5", 5.5, "5.5"],
    ]
    output = tabular_data.format_table(data)
    assert output == "| ## | 5 | 5 | 5.5 | 5.5 |\n| ## | 5 | 5 | 5.5 | 5.5 |"


TARGET_USERS_TABLE = """
| age  | is_admin | realname | role        | username  |
| ---- | -------- | -------- | ----------- | --------- |
|   13 |          | Andrew   |             | hunterx   |
|      |     True | Alice    |             | alice32   |
|      |          |          | game_master | natural20 |
""".strip()

def test_convert_dicts_to_table():
    output = tabular_data.format_table(tabular_data.convert_dicts_to_table(data.USERS), has_header=True)
    assert output == TARGET_USERS_TABLE
