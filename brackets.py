# Function to check if 'open' and 'close' characters form a valid bracket pair
def arePairs(open, close):
    if open == '[' and close == ']':
        return True
    if open == '{' and close == '}':
        return True
    if open == '(' and close == ')':
        return True
    return False

# Function to check if the input string 'A' contains balanced brackets
def Balanced(A):
    # Initialize an empty stack to keep track of opening brackets
    stack = []

    # Iterate through each character in the input string 'A'
    for i in range(len(A)):
        # If the current character is an opening bracket, push it onto the stack
        if A[i] == '[' or A[i] == '{' or A[i] == '(':
            stack.append(A[i])
        # If the current character is a closing bracket:
        elif A[i] == ']' or A[i] == '}' or A[i] == ')':
            # Check if it matches the most recent opening bracket in the stack
            # If it's a valid pair and the stack is not empty, pop the opening bracket from the stack
            if arePairs(stack[-1], A[i]) and len(stack) != 0:
                stack.pop()
            else:
                # If it doesn't match or the stack is empty, return False (unbalanced)
                return False

    # After processing all characters, check if the stack is empty
    if len(stack) == 0:
        return True  
    else:
        return False  


# Call the 'Balanced' function with an input string to check for balanced brackets
result = Balanced("({[()]})")
print(result) 


