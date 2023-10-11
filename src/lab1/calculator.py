"""Calculator"""

import re
from typing import Any, Dict

env: Dict[str, Any] = {}
env["locals"] = None
env["globals"] = None
env["__name__"] = None
env["__file__"] = None
env["__builtins__"] = None


def calculator(input_string: str):
    """calculate function"""
    if not re.search("[a-zA-Z=@!#$&^~`'\":;<>,]", input_string):
        try:
            result = eval(input_string, env)
            return result
        except ZeroDivisionError:
            return "You can not divide by zero"
        except SyntaxError:
            return "Please enter the correct expression"
    return "You used forbidden symbols"


if __name__ == "__main__":
    user_input = input("enter expression:")
    output = calculator(user_input)
    print(output)
