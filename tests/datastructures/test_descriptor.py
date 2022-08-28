import pytest

from python_properly.datastructures.descriptor import VarChar


def test_varchar():
    class DBTable:
        ...

    class Person(DBTable):
        name = VarChar()
        address = VarChar()

    person = Person()
    person.name = "Johnny Klarkson"

    with pytest.raises(TypeError):
        person.address = 1

    maxlength_string = "H" * 65_535
    person.address = maxlength_string

    with pytest.raises(ValueError):
        person.address = maxlength_string + "H"
