"""Calculator"""  

user_input = input("enter expression:")

env = {}
env["locals"] = None
env["globals"] = None
env["__name__"] = None
env["__file__"] = None
env["__builtins__"] = None

if 'os' not in user_input:
    result = eval(user_input, env)
    print(result)
