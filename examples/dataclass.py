
# This is a normal data class:

class User:
    def __init__(self,
        uid: int,
        username: str,
        given_name: str,
        family_name: str,
        is_admin: bool
    ):
        self.uid         = uid
        self.username    = username
        self.given_name  = given_name
        self.family_name = family_name
        self.is_admin    = is_admin

bob = User(5, "bob42", "Bob", "Builderson", False)
print(bob)


# ... but repetition sucks, lets use `dataclasses`

from dataclasses import dataclass

@dataclass
class User:
    uid: int
    username: str
    given_name: str
    family_name: str
    is_admin: bool

bob = User(5, "bob42", "Bob", "Builderson", False)
print(bob)


# Dataclasses can be compared

@dataclass()
class User:
    given_name: str
    family_name: str
    is_admin: bool

bob1  = User("Bob",   "Builderson",      False)
bob2  = User("Bob",   "Builderson",      False)
bob3  = User("Bob",   "Builderdaughter", False)

print(f"""
{(bob1 == bob2 ) = }
{(bob1 == bob3 ) = }
""")


# and even be lexicographically ordered

@dataclass(order=True)
class User:
    given_name: str
    family_name: str
    is_admin: bool

bob1  = User("Bob",   "Builderson",      False)
bob2  = User("Bob",   "Builderson",      True)
bob3  = User("Bob",   "Builderdaughter", False)
alice = User("Alice", "Missisipi",       False)
maud  = User("Maud",  "Gjerterud",       False)

print(*sorted([bob1, bob2, bob3, alice, maud]), sep="\n")
