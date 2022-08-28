import pytest

from python_properly.datastructures.descriptor import Person


def test_varchar():
    person = Person()
    person.name = "Johnny Klarkson"

    with pytest.raises(TypeError):
        person.address = 1

    maxlength_string = "H" * 65_535
    person.address = maxlength_string

    with pytest.raises(ValueError):
        person.address = maxlength_string + "H"
