from python_properly.problems.copy_vs_reference_part2  import User

# you can run these tests like so:
#   $ poetry run pytest tests/problems/test_copy_vs_reference_part2.py -x -v


def test_copy():
    bob1 = User("Bob Kaare", "bob42", ["moderator"])
    bob2 = bob1.make_copy()

    assert bob1 is not bob2, "the 'copy' is simply a reference"

    assert bob1.name     == bob2.name,     "the copy is not equal the original"
    assert bob1.username == bob2.username, "the copy is not equal the original"
    assert bob1.roles    == bob2.roles,    "the copy is not equal the original"

    bob2.add_role("janitor")
    assert "janitor"     in bob2.roles, "add_role is broken"
    assert "janitor"     in bob1.roles, "add_role did not affect the original"

    bob1.add_role("superstar")
    assert "superstar"     in bob2.roles, "add_role did not affect the copy"

    assert bob1.roles is     bob2.roles, "the copy is a deep copy"

def test_deep_copy():
    bob1 = User("Bob Kaare", "bob42", ["moderator"])
    bob2 = bob1.make_deep_copy()

    assert bob1 is not bob2, "the copy is simply a reference"

    assert bob1.name     == bob2.name,     "the deep copy is not equal the original"
    assert bob1.username == bob2.username, "the deep copy is not equal the original"
    assert bob1.roles    == bob2.roles,    "the deep copy is not equal the original"

    bob2.add_role("janitor")
    assert "janitor"     in bob2.roles, "add_role is broken"
    assert "janitor" not in bob1.roles, "add_role affected the original"

    bob1.add_role("superstar")
    assert "superstar" not in bob2.roles, "add_role affected the deep copy"

    assert bob1.roles is not bob2.roles, "the 'deep copy' is not a deep copy"
