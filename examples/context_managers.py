from contextlib import contextmanager

class MyContextManager:
    def __init__(self, argument1, argument2):
        self.argument1 = argument2
        self.argument2 = argument2

    def __enter__(self):
        print("MyContextManager.__enter__")
        return 42

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("MyContextManager.__exit__")
        print(f"  exc_type      = {exc_type!r}")
        print(f"  exc_value     = {exc_value!r}")
        print(f"  exc_traceback = {exc_traceback!r}")

with MyContextManager(1, 2) as value:
    print(f"value = {value!r}")

print()
print("="*20)
print()


try:
    with MyContextManager(1, 2) as value:
        raise Exception("this is a test")
except:
    pass

print()
print("="*40)
print()

@contextmanager
def my_context_manager(argument1, argument2):
    print("my_context_manager begin")
    try:
        yield 42
    except Exception as e:
        print("exception caught:", e)
    else:
        print("no exception!")
    print("my_context_manager end")

with my_context_manager(1, 2) as value:
    print(f"value = {value!r}")

print()
print("="*20)
print()

try:
    with my_context_manager(1, 2) as value:
        raise Exception("this is a test")
except:
    pass
