from functools import wraps
def make_upper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) == str:
                arg = arg.upper()
        for kwarg in kwargs:
            if type(kwarg) == str:
                kwargs[kwarg] = kwargs[kwarg].upper()
        result = func(*args, **kwargs)
        if type(result) == str:
            result = result.upper()
        return result
    return wrapper

@make_upper
def make_lower(string="Hello World"):
    print(f"making '{string}' lowercase")
    return string.lower()

print(make_lower())
print(make_lower("it works!"))
