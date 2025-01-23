def decor(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        func(*args, **kwargs)
        print("After calling the function")
    return wrapper

@decor
def my_func():
    print("Inside the function")

my_func()

# *args example
@decor
def fun(*args):
    print( sum(args))

fun(1, 2, 3, 4)
fun(5, 10, 15)

# **kwargs example
@decor
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)