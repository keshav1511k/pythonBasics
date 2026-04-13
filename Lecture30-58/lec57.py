# Decorators = A function that extends the behaviour of another another function without modifying the base function
# Pass the base function as an argument to the decorator

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinklers..")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge..")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream.")

get_ice_cream("chocolate")


# In this we use args and kwargs to pass arguments of any type as here we just pass flavour of the ice cream.