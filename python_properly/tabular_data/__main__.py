from . import format_table, convert_dicts_to_table, data

# You can run this module as follow:
#   $ poetry run python -m python_properly.tabular_data

if __name__ == "__main__":
    print(
        format_table(list(data.generate_people(20, add_header=True)), has_header=True, reverse=True)
    )
    print()
    print(
        format_table(convert_dicts_to_table(data.USERS), has_header=True)
    )
