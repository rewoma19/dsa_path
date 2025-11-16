class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize empty stack that will later store some brackets
        stack = []

        # Dictionary of matching closing and opening brackets
        closing_to_opening = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        # Loop through the given string of parentheses
        for char in s:
            # push the current character unto the stack if it is an opening bracket
            if char in closing_to_opening.values():
                stack.append(char)
            else:
                # first check is the stack is not empty
                # Then check if the opening bracket at the top of the stack matches with the current char that is a closing bracket
                # If so, pop from the stack
                if stack and (stack[-1] == closing_to_opening[char]):
                    stack.pop()
                else:
                    # If not, return false
                    return False

        # The strng will be valid if the stack is empty at the end
        return len(stack) == 0
    