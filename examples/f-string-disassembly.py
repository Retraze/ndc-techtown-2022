my_value = "foo"
print("my_value =,", repr(my_value))
print(f"{my_value = }")

# In general, f-strings are compact, and fast.

# f-strings has access to the current scope, and may perform arbitrary computations

from datetime import datetime
a = 5
b = "foo"
c = datetime.now()
print("a is {!r}, b is {!r}, c is {}".format(a, b, c))
print("a is {a!r}, b is {b!r}, c is {c}".format(a=a, b=b, c=c))
print("a is {a!r}, b is {b!r}, c is {c}".format(**locals()))
print(f"a is {a!r}, b is {b!r}, c is {c}")



# dissasembly time!

print()

# helper decorator
import dis, inspect, textwrap
def disassemble(func):
    print("====", func.__name__.replace("_", " ").capitalize(), "====")
    print()
    print(*textwrap.dedent(inspect.getsource(func)).splitlines()[2:], sep="\n")
    print()
    print(f"output: {func()!r}")
    print()
    dis.dis(func)
    print()
    return func

a = 5
b = "foo"

@disassemble
def the_concat_way():
    return "a is" + repr(a) + ", b is " + repr(b)

@disassemble
def the_join_way():
    return "".join(["a is", repr(a), ", b is ", repr(b)])

@disassemble
def the_sprintf_way():
    return "a is %r, b is %r" % (a, b)

@disassemble
def the_format_way():
    return "a is {!r}, b is {!r}".format(a, b)

@disassemble
def the_format_way_named():
    return "a is {a!r}, b is {b!r}".format(a=a, b=b)

@disassemble
def the_fstring_way():
    return f"a is {a!r}, b is {b!r}"

@disassemble
def the_fstring_way_sans_repr():
    return f"a is {a}, b is {b}"
