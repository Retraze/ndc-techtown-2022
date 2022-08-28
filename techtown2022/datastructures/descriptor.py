from abc import ABC, abstractmethod

# from https://docs.python.org/3/howto/descriptor.html
class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


# implementation
class VarChar(Validator):
    MAX_BYTE_LEN = 65_535

    def validate(self, s):
        if type(s) != str:
            raise TypeError("Must be str")
        if len(s.encode("utf-8")) > self.MAX_BYTE_LEN:
            raise ValueError(f"String exceeds {self.MAX_BYTE_LEN} bytes")
