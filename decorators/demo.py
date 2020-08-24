# Decorators

def outer_function(msg):
    def inner_funciton():
        print(msg)

    return inner_funciton

hi_func = outer_function("Hi")

bye_func = outer_function("Bye")

hi_func()

bye_func()

