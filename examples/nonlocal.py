import traceback

# the case for `global` and `nonlocal`

global_variable = 5

# This is fine, we're only reading
def read_global():
    print(global_variable)

# This is not fine, as we're writing to it.
def bump_global_error():
    global_variable += 1

# This is fine, since we've decleared the variable to be a global
def bump_global():
    global global_variable
    global_variable += 1


print("running read_global...")
try:
    read_global()
except:
    traceback.print_exc()
print()

print("running bump_global_error...")
try:
    bump_global_error()
except:
    traceback.print_exc()
print()

print("running bump_global...")
try:
    bump_global()
except:
    traceback.print_exc()
print()


# same goes for nonlocal variables
def main():

    nonlocal_variable = 7

    # This is fine, we're only reading
    def read_nonlocal():
        print(nonlocal_variable)

    # This is not fine, as we're writing to it.
    def bump_nonlocal_error():
        nonlocal_variable += 1

    # This is fine, since we've decleared the variable to be a nonlocal
    def bump_nonlocal():
        nonlocal nonlocal_variable
        nonlocal_variable += 1



    print("running read_nonlocal...")
    try:
        read_nonlocal()
    except:
        traceback.print_exc()
    print()

    print("running bump_nonlocal_error...")
    try:
        bump_nonlocal_error()
    except:
        traceback.print_exc()
    print()

    print("running bump_nonlocal...")
    try:
        bump_nonlocal()
    except:
        traceback.print_exc()
    print()

main()
