from python_properly.problems.copy_vs_reference_part1  import User

# you can run these tests like so:
#   $ poetry run pytest tests/problems/test_copy_vs_reference_part1.py -x -v


def test_duplicate():
    bob1 = User("Bob Kaare", "bob42", ["moderator"])
    bob2 = bob1.duplicate()

    assert bob1 is not bob2, "the duplicate is simply a reference"

    assert bob1.name     == bob2.name,     "the duplicate is not equal the original"
    assert bob1.username == bob2.username, "the duplicate is not equal the original"
    assert bob1.roles    == bob2.roles,    "the duplicate is not equal the original"

    bob2.add_role("janitor")
    assert "janitor"     in bob2.roles, "add_role is broken"
    assert "janitor" not in bob1.roles, "add_role affected the original"

    bob1.add_role("superstar")
    assert "superstar" not in bob2.roles, "add_role affected the duplicate"

    assert bob1.roles is not bob2.roles, "the duplicate is not a deep copy"
