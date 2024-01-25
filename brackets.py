def Balanced(code):
    # Initialize an empty stack to keep track of opening brackets
    stack = []

    # Iterate through each character in the code
    line_count = 1
    char_count = 0
    for line in code.split('\n'):
        # Iterate through each character in the line
        for char in line:
            char_count += 1
            # If the current character is an opening bracket, push it onto the stack
            if char in ['(', '[', '{']:
                stack.append((char, line_count, char_count))  # Store the bracket, line number, and character position
            # If the current character is a closing bracket:
            elif char in [')', ']', '}']:
                # Check if it matches the most recent opening bracket in the stack
                # If it's a valid pair and the stack is not empty, pop the opening bracket from the stack
                if len(stack) != 0 and arePairs(stack[-1][0], char):
                    stack.pop()
                else:
                    # If it doesn't match or the stack is empty, return the position of the unbalanced bracket
                    return False, stack[-1][1], stack[-1][2]

        # Reset character count for the next line
        char_count = 0
        line_count += 1

    # After processing all characters, check if the stack is empty
    if len(stack) == 0:
        return True, None, None  # Code is balanced
    else:
        # Return the position of the last unmatched opening bracket
        return False, stack[-1][1], stack[-1][2]

# Example usage with a multiline code snippet
code_snippet = """
def example_function():
    if condition:
        print("Hello, World!")
    else:
        print("Unbalanced brackets!")
"""
result, line_number, position_in_line = Balanced(code_snippet)

if result:
    print("The brackets are balanced.")
else:
    print(f"Unbalanced brackets at line {line_number-1}, position {position_in_line}.")
