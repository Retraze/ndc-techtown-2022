# Define some exceptions

class MyException(Exception):
    pass

class MyOtherException(Exception):
    pass

# Try raising some, and see how they are caught

try:
    raise MyException()
except Exception as e:
    print(type(e), "-", str(e))
except MyException as e:
    print(type(e), "-", str(e))
except MyOtherException as e:
    print(type(e), "-", str(e))

try:
    raise MyException()
except MyException as e:
    print(type(e), "-", str(e))
except MyOtherException as e:
    print(type(e), "-", str(e))
except Exception as e:
    print(type(e), "-", str(e))

try:
    raise MyOtherException()
except MyException as e:
    print(type(e), "-", str(e))
except MyOtherException as e:
    print(type(e), "-", str(e))
except Exception as e:
    print(type(e), "-", str(e))


# else

print()
print("="*20, "else", "="*20)
print()

for i in [5, 0]:
    print("For start")
    try:
        print(10 / i)
    except Exception as e:
        print(type(e), "-", str(e))
    else:
        print("Try else")
    print("For end")


# finally

print()
print("="*20, "finally", "="*20)
print()

for i in [5, 0]:
    print("For start")
    try:
        print(10 / i)
    except Exception as e:
        print(type(e), "-", str(e))
    else:
        print("Try else")
    finally:
        print("Try finally")
    print("For end")


# try-finally use-case

if False: # do not run this example

    file_handle = open("some_file_name.txt", "w")
    try:
        for i in [5, 0]:
            file_handle.write("The result of 10 divided by {i} is ")
            file_handle.write(str(10 / i))
            file_handle.write("\n")
    finally:
        # the finally block is often used for required cleanup
        file_handle.flush()
        file_handle.close()

# Printing or logging tracebacks without aborting

print()
print("="*20, "tracebacks", "="*20)
print()


import sys, traceback

try:
    5 / 0
except: # catch all
    # retrieves the traceback of the active exception as a string
    # and prints it to stderr
    print(traceback.format_exc(), file=sys.stderr)

print("We're still running!")




# Reraising exceptions

print()
print("="*20, "raise from", "="*20)
print()



def get_user():
    raise FileNotFoundError("not found")

class InternalServerError(RuntimeError):
    pass

def public_function():
    try:
        get_user()
    except Exception as e:
        raise InternalServerError("Error: " + str(e)) from None

try:
    public_function()
except:
    traceback.print_exc()

print()
print("="*20)
print()


def public_function():
    try:
        get_user()
    except Exception as e:
        raise InternalServerError(
            "Error: " + type(e).__name__ + ": " + str(e)) from None

try:
    public_function()
except:
    traceback.print_exc()

print()
print("="*20)
print()


def public_function():
    try:
        get_user()
    except Exception as e:
        raise InternalServerError from e

try:
    public_function()
except:
    traceback.print_exc()

print()
print("="*20)
print()


def public_function():
    try:
        get_user()
    except Exception as e:
        raise InternalServerError

try:
    public_function()
except:
    traceback.print_exc()


# traceback hooks

print()
print("="*20, "tracebacks hooks", "="*20)
print()



# This is kinda what happens the an uncaught exception is raised:
if False: # (do not run)
    sys.excepthook(*sys.exc_info())

sys.excepthook # can be overrided!

from rich.traceback import install
install()
5 / 0
