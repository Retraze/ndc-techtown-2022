import traceback, sys

my_sequence = ["a", "b", "c"]

# iter() can convert sequences to iterators
my_iterator = iter(my_sequence)

try:
    while True:
        print(next(my_iterator))
except:
    traceback.print_exc(file=sys.stdout)


print()
print("="*20)
print()


class MySequence():
    def __getitem__(self, index):
        if index == 0: return "a"
        if index == 1: return "b"
        if index == 2: return "c"
        raise IndexError

my_sequence = MySequence()
my_iterator = iter(my_sequence)

try:
    while True:
        print(next(my_iterator))
except:
    traceback.print_exc(file=sys.stdout)


print()
print("="*20)
print()


my_container = ["a", "b", "c"]
my_iterator = iter(my_container)
for _ in range(20): # we will never get a StopIteration
    val = next(my_iterator)
    my_container.append(val)
    print(val)



print()
print("="*20)
print()


def my_generator():
    print("my_generator start")
    for _ in range(3):
        print("my_generator yield")
        yield 42
        print("my_generator resume")
    print("my_generator end")
    return "return value"

print("generator init")
generator = my_generator()
while True:
    print("next")
    try:
        value = next(generator)
    except:
        traceback.print_exc(file=sys.stdout)
        break
    print(f"value = {value}")
print("while end")


print()
print("="*20)
print()


print("generator init")
generator = my_generator()
print("for start")
for value in generator:
    print(f"value = {value}")
print("for end")



print()
print("="*20)
print()


print("generator init")
generator = my_generator()
print("list init")
mylist = list(generator)
print(f"mylist = {mylist}")


print()
print("="*20)
print()


def generator1(value):
    yield value,
    yield value, value
    yield value, value, value
    return value*2

def generator2(value):
    retval = yield from generator1(value)
    yield retval
    retval = yield from generator1(value*2)
    yield retval

for i in generator2("test"):
    print(i)
