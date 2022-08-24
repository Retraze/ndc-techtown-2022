from dis import dis
import rich
from rich.syntax import Syntax
import inspect


global_variable = 5

# enter a non-global scope
def main():

    nonlocal_variable = 5

    def my_function():
        print(global_variable)

    rich.print(Syntax(inspect.getsource(my_function), "python", theme="rrt", dedent=True))
    dis(my_function)
    print(f"\n{'='*20}\n")

    def my_function():
        print(nonlocal_variable)

    rich.print(Syntax(inspect.getsource(my_function), "python", theme="rrt", dedent=True))
    dis(my_function)
    print(f"\n{'='*20}\n")

    def my_function():
        print(nonlocal_variable)
        nonlocal_variable = nonlocal_variable + 2
        print(nonlocal_variable)

    rich.print(Syntax(inspect.getsource(my_function), "python", theme="rrt", dedent=True))
    dis(my_function)
    print(f"\n{'='*20}\n")

    def my_function():
        nonlocal nonlocal_variable
        print(nonlocal_variable)
        nonlocal_variable = nonlocal_variable + 2
        print(nonlocal_variable)

    rich.print(Syntax(inspect.getsource(my_function), "python", theme="rrt", dedent=True))
    dis(my_function)



if __name__ == "__main__":
    main()
