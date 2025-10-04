# Function to convert a PascalCase or camelCase string into snake_case
def convert_to_snake_case(pascal_or_camel_cased_string):

    # Build a list of characters:
    # - If the character is uppercase → prepend '_' and make it lowercase
    # - Otherwise → keep the character as it is
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    # Join the list back into a string
    # strip('_') removes any leading underscore (from the very first uppercase letter)
    return ''.join(snake_cased_char_list).strip('_')


def main():
    # Example: PascalCase → snake_case
    print(convert_to_snake_case('IAmAPascalCasedString'))  # Output: i_am_a_pascal_cased_string

    # Example: camelCase → snake_case
    print(convert_to_snake_case('camelCaseExample'))       # Output: camel_case_example


# Run program
main()
